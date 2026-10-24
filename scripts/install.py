#!/usr/bin/env python3
"""Install a local course copy. No network requests or dependency installation."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile


def install_files(source):
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    paths = manifest["install_files"]
    if not paths or len(paths) != len(set(paths)):
        raise ValueError("安装文件清单为空或重复")
    for item in paths:
        relative = Path(item)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("安装清单包含越界路径")
        candidate = source / relative
        if candidate.is_symlink() or not candidate.is_file():
            raise ValueError("安装清单中有缺失文件或符号链接: " + item)
        if source not in candidate.resolve().parents:
            raise ValueError("安装来源超出仓库")
    return paths


def main():
    parser = argparse.ArgumentParser(description="将当前仓库安装为本地 AI PM FDE School Skill")
    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--codex", action="store_true", help="安装到 ~/.codex/skills/ai-pm-fde-school")
    target.add_argument("--claude", action="store_true", help="安装到 ~/.claude/skills/ai-pm-fde-school")
    target.add_argument("--dir", type=Path, help="指定完整安装目标目录")
    parser.add_argument("--replace", action="store_true", help="覆盖清单中的已有文件，保留额外文件")
    parser.add_argument("--dry-run", action="store_true", help="仅查看计划，不写入")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1]
    if args.codex:
        destination = Path.home() / ".codex/skills/ai-pm-fde-school"
    elif args.claude:
        destination = Path.home() / ".claude/skills/ai-pm-fde-school"
    else:
        destination = args.dir.expanduser().absolute()
    try:
        files = install_files(source)
        resolved = destination.resolve()
        if resolved == source or source in resolved.parents or resolved in source.parents:
            raise ValueError("目标不能是源仓库、源仓库的父目录或子目录")
        if destination.is_symlink() or any(p.is_symlink() for p in destination.parents):
            raise ValueError("目标目录不能经过符号链接")
        if destination.exists() and not destination.is_dir():
            raise ValueError("目标已存在且不是目录")
        if destination.exists() and any(destination.iterdir()) and not args.replace:
            raise ValueError("目标非空；确认无须保留的课程手工修改后，可显式使用 --replace")
        # Validate every target before writing anything.
        for item in files:
            output = destination / item
            if output.is_symlink() or (output.exists() and not output.is_file()):
                raise ValueError("目标文件类型冲突: " + item)
            for parent in output.parents:
                if parent == destination:
                    break
                if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                    raise ValueError("目标父目录类型冲突: " + item)
        print("目标: " + str(destination))
        print("版本: " + json.loads((source / "manifest.json").read_text())["version"])
        print("文件数: " + str(len(files)))
        if args.dry_run:
            print("仅预览；未创建或修改文件。")
            return 0
        for item in files:
            output = destination / item
            output.parent.mkdir(parents=True, exist_ok=True)
            # Atomic per-file replacement; never remove extra user files.
            staging = None
            try:
                with tempfile.NamedTemporaryFile(dir=output.parent, delete=False) as stream:
                    staging = Path(stream.name)
                    stream.write((source / item).read_bytes())
                os.replace(staging, output)
            finally:
                if staging is not None and staging.exists():
                    staging.unlink()
        print("安装完成。学习进度独立保存；没有联网或修改其他 Skill。")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("安装停止: " + str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
