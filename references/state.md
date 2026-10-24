# 学习记录

学习记录只用于续学，默认不上传。

## 存放位置

有独立学习工作区时，放在该工作区的 `.learning/progress.json`，作品放 `.learning/outputs/`。在本仓库学习时 `.learning/` 已被 Git 忽略。

若没有可写的独立学习工作区，使用 `~/.ai-pm-fde-school/progress.json` 与 `~/.ai-pm-fde-school/outputs/`。不要写入 Skill 安装目录。已找到已有记录时沿用原位置，不同时维护两份。

开始续学时先检查文件是否存在；缺失按首次学习处理，不把缺失当错误。写前回读，合并已完成阶段，使用临时文件和替换方式保存；写失败时保留已有文件并在对话给续学摘要。

## 记录格式示例

```json
{
  "schema_version": 1,
  "course_version": "1.1.0",
  "mode": "guided-practice",
  "current_lesson": "delivery/02-discovery-diagnosis",
  "updated_at": "2026-10-24",
  "lessons": {
    "delivery/00-ai-pm-to-fde": {
      "status": "read",
      "review": null,
      "artifact": null
    },
    "delivery/01-public-research": {
      "status": "verified",
      "review": "事实与未知已分开，待验证项明确",
      "artifact": "outputs/01-research-brief.md"
    }
  },
  "open_questions": ["采购责任人尚未确认"],
  "next_action": "根据证据卡补充流程交接与主需求假设"
}
```

状态：`not-started` 未开始；`reading` 正在读；`read` 已阅读；`practicing` 练习中；`submitted` 有作品待评审；`verified` 通过教学评审；`skipped` 用户跳过。不能因讲过、用户回复“懂了”或模板字段已填写就自动改为 `verified`。

课程 ID 使用板块前缀避免重名：`ai-native/`、`foundations/`、`shared/`、`delivery/`。例如 `ai-native/03-portfolio-lab` 与 `delivery/03-ontology-solution` 不互相覆盖；附属实验可用 `foundations/freight-roleplay`。

`review` 没有实际评审时保持 `null`。`artifact` 指向本地脱敏作品；记录不嵌入客户原话、简历、合同或敏感数据。日期使用真实当前日期，示例日期不作为自动默认值。

不同课程版本迁移时保留旧记录，不自动把新增标准视为通过。需要时标记应复核的产物；不删除已完成作品。
