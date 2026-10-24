#!/usr/bin/env python3
"""Check course files, relative links and safe installation in a temporary folder."""

import csv
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


def main():
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    files = manifest["install_files"]
    require(len(files) == len(set(files)), "安装清单存在重复项")
    actual = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
                    if p.is_file() and not any(part.startswith(".") or part == "__pycache__"
                                              for part in p.relative_to(ROOT).parts))
    actual = sorted(actual + [".gitignore"])
    require(sorted(files) == actual, "正式文件与 manifest 安装清单不一致")
    require(len(list((ROOT / "references/lessons").glob("*.md"))) == 7, "应有七节交付进阶课")
    require(len(list((ROOT / "references/ai-native").glob("*.md"))) == 4, "应有四节 AI Native 课程")
    require(len(list((ROOT / "references/foundations").glob("0*.md"))) == 4, "应有四节 FDE 基础课")
    require(len(list((ROOT / "references/shared").glob("*.md"))) == 5, "应有五节共修课")
    require((ROOT / "references/foundations/freight-roleplay.md").is_file(), "货代角色练习缺失")
    require((ROOT / "labs/portfolio/index.html").is_file(), "本地作品页实验缺失")
    require(len(list((ROOT / "templates").glob("0*.md"))) == 5, "应有五份阶段模板")
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    require(skill.startswith("---\nname: ai-pm-fde-school\n"), "Skill 名称或元数据不一致")
    for item in files:
        path = ROOT / item
        require(path.is_file() and not path.is_symlink(), "文件缺失或使用符号链接: " + item)
        if not path.is_file() or path.suffix not in (".md", ".json", ".csv", ".py", ".html"):
            continue
        content = path.read_text(encoding="utf-8")
        # Generic publication checks; not an exhaustive privacy audit.
        require(not re.search(r"/(?:Users|home)/[^\s/]+/", content), "包含本机绝对路径: " + item)
        require(not re.search(r"\b1[3-9]\d{9}\b", content), "可能包含手机号: " + item)
        require(not re.search(r"(?:ghp_|github_pat_|sk-)[A-Za-z0-9_]{20,}", content), "可能包含凭据: " + item)
        if path.suffix == ".md":
            body = re.sub(r"```[\s\S]*?```", "", content)
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
                if re.match(r"[a-z][a-z0-9+.-]*:", link, re.I) or link.startswith("#"):
                    continue
                target = link.split("#", 1)[0].strip("<>")
                if target:
                    resolved = (path.parent / target).resolve()
                    require(ROOT in resolved.parents and resolved.exists(), item + " 无效链接: " + link)
    ignored = (ROOT / ".gitignore").read_text()
    require(".learning/" in ignored and ".local/" in ignored, "学习记录和内部状态必须忽略")
    with (ROOT / "cases/manufacturing-quote/sample-data.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    require(len(rows) == 10 and len({r["case_id"] for r in rows}) == 10, "案例应有十个独立样本")
    require(all(r["data_kind"] == "synthetic" for r in rows), "样本必须标明合成")
    expected = {"baseline_active_min": 290, "pilot_prepare_min": 47,
                "pilot_review_min": 74, "pilot_correction_min": 17,
                "pilot_operations_min": 10, "first_pass_fields_correct": 95,
                "fields_checked": 100}
    totals = {key: sum(int(row[key]) for row in rows) for key in expected}
    require(totals == expected, "案例合计与参考答案不一致")
    require(all(int(r["first_pass_fields_correct"]) <= int(r["fields_checked"]) for r in rows),
            "正确字段数超出分母")
    require(sum(r["exception_required"] == "true" for r in rows) == 6 and
            all(r["exception_required"] == r["exception_routed"] for r in rows), "异常标签与案例不一致")
    require(all(int(r[key]) >= 0 for r in rows for key in expected), "样本出现负数")
    with tempfile.TemporaryDirectory(prefix="fde-school-check-") as temp:
        destination = Path(temp).resolve() / "installed"
        command = [sys.executable, str(ROOT / "scripts/install.py"), "--dir", str(destination)]
        preview = subprocess.run(command + ["--dry-run"], capture_output=True, text=True)
        require(preview.returncode == 0 and not destination.exists(), "安装预览发生写入或失败")
        installed = subprocess.run(command, capture_output=True, text=True)
        require(installed.returncode == 0, "临时安装失败: " + installed.stderr)
        if installed.returncode == 0:
            require(all((destination / item).read_bytes() == (ROOT / item).read_bytes()
                        for item in files), "临时安装内容不一致")
            existing = subprocess.run(command, capture_output=True, text=True)
            require(existing.returncode != 0, "安装器默认覆盖了已有目录")
            extra = destination / "learner-note.txt"
            extra.write_text("preserve", encoding="utf-8")
            replaced = subprocess.run(command + ["--replace"], capture_output=True, text=True)
            require(replaced.returncode == 0 and extra.read_text() == "preserve", "替换安装损坏额外文件")
        nested = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--dir", str(ROOT / "unsafe-install"), "--dry-run"],
                                capture_output=True, text=True)
        require(nested.returncode != 0, "未拒绝将安装写进源仓库")
    if errors:
        for error in errors:
            print("FAIL: " + error)
        return 1
    print("PASS: 清单、课程结构、相对链接、合成数据口径、公开标记、临时安装及覆盖保护。")
    print("范围: 未验证真实学习效果、实际模型准确率或客户采用。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
