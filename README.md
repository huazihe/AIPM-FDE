# AIPM-FDE

覆盖 AI Native、FDE 基础、GitHub 协作、企业沟通与解决方案交付的学习仓库，重点服务已有 AI 产品经理基础的学习者。

把需求分析、Agent / RAG、产品设计与快速原型能力，延伸到客户现场：看懂业务、确认真实问题、定义业务规则、验证可行性、推进交付和采用，再把经验转成可复用的产品能力。

全库包含 **20 节课程**。基础与共修课按需学习；进阶主线围绕同一个教学案例完成五份交付物，最终形成一套可以用于下一次项目的工作方法。AI 导师 Skill 的调用名为 `ai-pm-fde-school`。

## 完整课程体系

| 板块 | 课程 | 解决什么问题 |
|---|---|---|
| AI Native · 4 节 | Agent 优先与零 Token 设计、AI 工作区协作、本地项目作品页实操、产品延伸 | 理解产品如何与用户自己的 Agent 协作，亲手运行一个结果承载工具 |
| FDE 基础 · 4 节 | 岗位与能力边界、客户九宫格、证据式能力诊断、市场与入局判断 | 理解 FDE、判断自己缺什么、如何选择客户与职业切入点 |
| GitHub 共修 · 2 节 | 协作概念、第一个 Issue 与 PR | 看懂版本、分工、变更和验收，完成一次协作练习 |
| 企业沟通共修 · 3 节 | 会前准备、会中信任与边界、会后推进试点 | 将技术能力表达为业务机会，处理质疑并推进有边界的验证 |
| 解决方案型 FDE 进阶 · 7 节 | 从 AI PM 转向现场，到五步交付与综合迁移 | 完成调研、诊断、建模、验证、采用和产品回流 |

完整课表及入口见 [学习路线](references/course.md)。还提供[货代需求访谈角色练习](references/foundations/freight-roleplay.md)、[本地项目作品页](labs/portfolio/README.md)和两类跨场景任务。

## 适合谁

- 已参与过 AI 产品设计、需求分析或原型验证，准备承担企业客户项目。
- 能讨论模型、提示词、工具调用或 RAG 的选择，但希望补上业务建模与现场交付。
- 正在从产品经理、售前或业务分析转向解决方案型 FDE。

课程不要求你独自负责全部研发、部署和运维；要求你能明确责任、判断风险、提出可验证的需求，并与工程团队协作。已有系统架构、工程基础或行业经验可以帮助你跳过熟悉部分。

## 学完要交付什么

| 阶段 | 要回答的问题 | 可交付成果 |
|---|---|---|
| 1. 公开资料调研 | 我对这家企业的理解有哪些证据，哪些需要现场确认？ | 调研简报与访谈假设 |
| 2. 客户需求整理与诊断 | 谁在什么流程里遇到什么问题，值得先解决哪一个？ | 客户档案、流程与需求诊断卡 |
| 3. Ontology 与解决方案 | 对象、字段、关系、规则和例外是什么，AI 负责哪一段？ | 业务模型与方案边界 |
| 4. POC 验证与落地交付 | 怎样证明方案有效，什么条件下可以交给真实用户？ | POC 章程、评测与工程交接清单 |
| 5. 持续迭代与产品回流 | 用户是否持续使用，哪些经验可以复用？ | 采用记录、反馈分类与产品回流提案 |

公开资料调研与访谈后的需求诊断分开进行。第五步同时保留客户问题解决和跨客户资产沉淀两项责任。

## 从这里开始

**直接阅读**：[学习路线](references/course.md)。已有 AI PM 基础、准备客户交付，可从[进阶第 0 课](references/lessons/00-ai-pm-to-fde.md)开始；想先了解 AI Native 或 FDE，可以进入对应基础板块。

**让 AI 带学**：下载或克隆本仓库，在 Codex / Claude Code 中打开这个目录，发送：

```text
读取当前仓库的 SKILL.md，按 AI PM FDE School 带我学习。
我已有 AI 产品经理基础。先用仓库的虚构制造业案例示范，再让我完成第一份交付物。
```

**带自己的项目**：使用经过授权、已脱敏的材料。可以直接说“评审我的需求诊断卡”或“帮我把这个流程建成 Ontology”，AI 会进入对应阶段，不强制从第一课重读。

默认不需要安装、不需要额外模型 API Key，也没有课程方的推理服务。使用 AI 导师时，消耗你所使用的 AI 工具额度。

## 解决方案型 FDE 进阶：7 节

| 课 | 内容 | 练习产物 |
|---|---|---|
| [00](references/lessons/00-ai-pm-to-fde.md) | 从 AI PM 到解决方案型 FDE：责任与能力迁移 | 个人能力与交付责任图 |
| [01](references/lessons/01-public-research.md) | 公开资料调研：带着假设进现场 | 调研简报 |
| [02](references/lessons/02-discovery-diagnosis.md) | 需求整理与诊断：还原流程、判断价值与采购条件 | 需求诊断卡 |
| [03](references/lessons/03-ontology-solution.md) | Ontology 与解决方案：把隐性经验变成明确规则 | 业务模型与方案边界 |
| [04](references/lessons/04-poc-delivery.md) | POC 与交付：从可演示走向可验证、可接手 | POC 章程与交接包 |
| [05](references/lessons/05-adoption-feedback.md) | 客户采用与产品回流：跟进效果、分流反馈 | 采用与产品回流记录 |
| [06](references/lessons/06-capstone.md) | 综合项目：串起五步并迁移到新场景 | 五份成果与迁移说明 |

## 怎么学

**讲解 → 示范 → 实践 → 证据评审 → 复盘迁移。**

先给完整解释和示范；练习可以选择做。课程根据你已有的作品、问题和反馈调整顺序，不用连续盘问来建立画像。跳过练习可记录为“已阅读”，实际完成并经评审后才记录为“已验证”。

- [制造企业 M 案例](cases/manufacturing-quote/brief.md)：证据卡、合成数据和参考答案，覆盖五步流程。
- [本地项目作品页](labs/portfolio/README.md)：无需联网即可展示结构化成果，体验 Agent 生成内容、工具承载结果的分工。
- [跨场景迁移挑战](cases/transfer-challenge.md)：把方法迁移到知识密集型报告审核。
- [五份可复制模板](templates/README.md)：可以直接用在练习或已授权项目。
- [成果评审标准](references/rubric.md)：看证据、决策与交付完整性，不以字数或术语数量判分。
- [学习方法](references/learning-method.md)：用已有作品定位起点，逐步减少示范，最后用跨场景迁移检查理解。

所有案例、角色、数据和效果数字都是教学构造，不对应真实客户，不是实际模型测试或已实现的业务收益。完成课程表示完成学习练习，不构成岗位认证。

## 可选：安装为本地 Skill

在仓库根目录执行，要求 Python 3.9 或更高版本：

```bash
python3 scripts/install.py --codex
# 或：python3 scripts/install.py --claude
```

默认分别安装到 `~/.codex/skills/ai-pm-fde-school` 或 `~/.claude/skills/ai-pm-fde-school`。可先加 `--dry-run` 查看计划；已存在时默认停止，只有显式加 `--replace` 才覆盖清单中的文件。安装器不联网、不修改账号、不自动更新，也不安装运行依赖。

安装后可以明确调用 `$ai-pm-fde-school`，或告诉助手“使用 ai-pm-fde-school 带我学习解决方案型 FDE”。实际调用方式取决于宿主工具是否已识别新 Skill。

学习记录保存在当前学习工作区的 `.learning/`；没有独立工作区时使用 `~/.ai-pm-fde-school/`。安装目录不存学习进度。进度只在本机保存，不自动上传 GitHub。

## 仓库结构

```text
SKILL.md                 AI 导师入口
references/course.md     学习路线与跳课规则
references/ai-native/    四节 AI Native 课程
references/foundations/  四节 FDE 基础与角色练习
references/shared/       GitHub 与企业沟通共修
references/lessons/      七节解决方案交付进阶课
references/rubric.md     成果评审标准
references/state.md      学习记录约定
cases/                   合成案例、数据、参考答案与迁移题
labs/portfolio/          可离线运行的项目作品页实验
templates/               五步交付模板
scripts/install.py       可选本地安装器
scripts/check.py         内容结构与公开文件检查
manifest.json            版本和安装文件清单
```

维护课程的方法见 [维护说明](docs/maintaining.md)。
