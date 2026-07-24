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

请完整保留每个 Skill 目录中的 SKILL.md、agents/openai.yaml 和 references 等配套文件。

不要把英文目录名或 SKILL.md 中的 name 改成中文；中文显示名已经配置在 agents/openai.yaml 中。

安装完成后，请确认两个 Skill 都能被发现，并告诉我它们的中文显示名和英文运行名；从下一轮对话开始使用。
```

也可以只安装其中一个，把另一个路径删掉即可。

## 安装后：给英文运行名套上中文外壳

这两个 Skill 已经采用“**英文运行名 + 中文显示名**”的双轨方案，安装者不需要再手工重命名：

| 中文显示名 | 英文运行名 | 最稳妥的显式调用 | 中文自然语言用法 |
|---|---|---|---|
| 需求榨干 | `grill-requirements` | `$grill-requirements` | `用需求榨干把这个需求问透` |
| 提示词增强 | `enhance-prompt` | `$enhance-prompt` | `用提示词增强优化下面这段话` |

- `SKILL.md` 中的英文 `name` 和英文目录名是稳定运行标识。按照当前 Skill 命名规范，它们使用小写英文字母、数字和连字符，且目录名应与 `name` 一致。
- `agents/openai.yaml` 中的中文 `display_name` 是给技能列表和界面标签看的“中文外壳”。在支持这项元数据的 Codex 界面中，会显示“需求榨干”和“提示词增强”。
- 明确指定 Skill 时，推荐继续使用 `$grill-requirements` 和 `$enhance-prompt`。中文名负责易读展示和自然语言触发，不替代英文运行标识。
- 如果安装器只复制了 `SKILL.md`、漏掉 `agents/openai.yaml`，Skill 可能仍能运行，但中文显示名不会完整生效；因此应复制整个 Skill 目录。

这就是“把原来的英文外壳套上中文名字”的实际做法：**底层标识保持英文以保证兼容性，用户看到和理解的名称使用中文。**

## 手动安装

```bash
git clone https://github.com/nate2022-ai/nate-ai-skills.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R nate-ai-skills/skills/grill-requirements "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R nate-ai-skills/skills/enhance-prompt "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后请开启新一轮对话，让 Codex 重新发现 Skill。

## 像我一样使用

安装后新开一轮对话。第一次使用时建议明确写出英文运行名；Codex 界面可以显示中文名，但 `$` 后面的稳定调用名仍是英文。

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

## 两个 Skill 的中文改造方案

这里的“中文改造”不只是把标题翻译成中文，而是保留兼容的英文运行标识，同时根据中文用户与 Codex 的真实协作方式重做触发语义、工作流程和输出口径。

### 需求榨干：把 `grilling` 思路改造成中文需求决策流程

「需求榨干」的单题追问、决策树和“能查到的事实不反问用户”方法，受到 Matt Pocock 的 [`grilling` Skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) 启发；公开版本不是逐句翻译，而是进行了这些中文工作流改造：

- 默认一次只问一个真正会改变方案的问题；只有互相独立、同层级、低风险的问题才允许受控合并。
- 每一题都给出推荐答案、理由和主要取舍，减少用户理解技术选项的负担。
- 先读对话、项目文件、现行规则和本地事实，把“已确认事实 / 待验证判断 / 用户决策”分开。
- 持续更新真实问题、核心动机、目标、成功标准、范围和关键约束，并记录决策及冲突。
- 设置“整体理解至少 95% + 无高影响歧义 + 用户确认共同理解”的停止追问闸门。
- 最终输出带阶段、停车闸、验收证据和执行授权状态的详细规划；规划完成不等于已经获得实施授权。

它解决的不是“问题问得不够多”，而是中文业务沟通中常见的隐含前提、上下文遗漏和“AI 还没听懂就开始干”的问题。

### 提示词增强：把中文口头需求整理成可执行任务说明

「提示词增强」不是某个英文 Skill 的逐句翻译，而是围绕中文用户给 Codex 下任务时的真实表达习惯设计：

- 保留原意和任务性质：分析仍是分析，讨论仍是讨论，不擅自升级成执行或外部写入。
- 简单需求只做轻量整理；复杂任务才按“目标 / 背景 / 限制 / 完成标准”四段式展开。
- 优先利用当前对话、用户点名的文件和项目规则，不编造背景，也不把能查到的信息变成反问。
- 把“高质量、专业、完善”等空话改成可检查的完成条件、验证动作和证据要求。
- 面向新对话时，只有模型选择明显影响效果才给简短建议，并且不声称已经替用户切换模型。
- 只有高难度软件开发任务才加入独立审查闭环；普通小改和非开发任务不会机械套用。

它的目标不是把提示词写得更长，而是让一段中文粗略想法变成**不失真、边界清楚、可以直接复制、完成后能够验收**的任务说明。

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
