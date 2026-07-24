# Nate AI Skills

两个从真实中文工作流中持续打磨的 AI Agent Skills：

- **需求榨干（`grill-requirements`）**：在实施前逐步问透真正会改变方案的决策，达成共同理解后再生成完整规划。
- **提示词增强（`enhance-prompt`）**：把粗略需求整理成清晰、可执行、可验收，又不改变原意的提示词。

这两个 Skill 主要面向 Codex，也可供采用相似 Agent Skills 目录规范的 AI 工具参考。

## 建立缘起

这些 Skill 不是一次性写出来的，而是在长期、高频使用 Codex 的过程中，围绕两个反复出现的问题逐步打磨：

1. AI 很容易在没有真正理解需求时就开始给方案或动手；
2. 用户脑中已经有目标，但原始表达往往缺少边界、背景和验收标准。

下面是其中一段 Codex 使用记录：

![Codex 使用记录](assets/codex-usage-overview.png)

后来，我在抖音分享了「需求榨干」的使用思路，评论区陆续有网友希望获得这两个 Skill。**这张评论区截图所代表的真实分享需求，是我建立并公开这个仓库的原因之一。**

<p align="center">
  <img src="assets/douyin-request-redacted.png" alt="网友希望获取 Skill 的评论区截图（已脱敏）" width="420">
</p>

> 隐私说明：公开图片已遮盖全部可识别的抖音昵称、`@用户名`、头像和回复对象；仓库中不保存原始未脱敏截图。

## 包含的 Skill

| Skill | 适用场景 | 核心特点 |
|---|---|---|
| [`grill-requirements`](skills/grill-requirements/) | 需求复杂、影响大、容易返工，或用户明确要求“把需求问透” | 先查事实；优先追问会让方案改道的问题；默认一次一问；每题给推荐；理解信心达到至少 95% 后才建议结束访谈 |
| [`enhance-prompt`](skills/enhance-prompt/) | 用户明确要求优化、重写或整理一段提示词 | 保留原意和任务性质；补清目标、背景、限制与完成标准；不擅自把讨论升级成执行 |

## 推荐安装方式：直接让 Codex 安装

把下面这段话复制给 Codex：

```text
请从 GitHub 仓库 https://github.com/nate2022-ai/nate-ai-skills 安装以下两个 Skill：

- skills/grill-requirements
- skills/enhance-prompt

安装完成后告诉我；从下一轮对话开始使用。
```

也可以只安装其中一个，把另一个路径删掉即可。

## 手动安装

```bash
git clone https://github.com/nate2022-ai/nate-ai-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R nate-ai-skills/skills/grill-requirements "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R nate-ai-skills/skills/enhance-prompt "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后请开启新一轮对话，让 Codex 重新发现 Skill。

## 使用示例

### 需求榨干

```text
使用 $grill-requirements 把这个需求问透。

默认一次只问一个真正会改变方案的问题；每题给出你的推荐答案和理由。先查能查到的事实，不要把事实问题反问给我。达成共同理解前不要实施，理解信心达到至少 95% 后再给出共同理解摘要。
```

适合：

- 新项目、关键业务流程或产品方案；
- 需求中存在大量隐含假设；
- 做错后的返工、安全或经营成本较高；
- 你希望 AI 先理解真实目标，再输出详细规划。

不适合：

- 目标已经清楚的一次性小任务；
- 只需简单改字、翻译或格式整理；
- 你已经明确授权并希望立即执行的低风险工作。

### 提示词增强

```text
使用 $enhance-prompt 优化下面这段提示词。保留我的原意和任务性质，不新增我没有提出的目标；补清必要的背景、限制和可检查的完成标准。默认只输出一段可直接复制的新提示词。

[在这里粘贴原始需求]
```

适合：

- 把一句粗略想法整理成新对话任务说明；
- 为分析、开发、文档或本地文件任务补充边界；
- 明确只读、禁止项、输出格式和验收证据；
- 减少 AI 因提示词含糊而自行扩张范围。

## 目录结构

```text
nate-ai-skills/
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── assets/
│   ├── codex-usage-overview.png
│   └── douyin-request-redacted.png
└── skills/
    ├── grill-requirements/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── references/final-plan-template.md
    └── enhance-prompt/
        ├── SKILL.md
        └── agents/openai.yaml
```

## 设计边界

- 「需求榨干」负责发现和解决高影响歧义，不把规划自动当成执行授权。
- 「提示词增强」负责整理用户已经表达出来的需求，不代替长时间的需求访谈。
- 两个 Skill 都要求区分事实、判断、用户决策和未知项。
- Skill 只提供工作方法，最终效果仍取决于模型能力、可见上下文、工具权限和任务资料质量。

## 来源与许可

- 本仓库使用 [MIT License](LICENSE)。
- 「需求榨干」的单题追问、决策树和“能查的事实不反问”方法受到 Matt Pocock 的 [`grilling` Skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) 启发。本仓库版本针对中文 AI 办公工作流重新设计，并增加了事实/决策分离、决策账本、停车闸、95% 理解闸和最终详细规划。
- 完整第三方来源与许可信息见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
