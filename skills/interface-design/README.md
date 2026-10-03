# 界面设计 · Interface Design

一个可独立安装的中文设计 Skill：设计、审查、改造和验收网页、移动端、原生及桌面界面；需要参考时，从设计奖和优秀作品中查找与当前问题相似的案例，再转化为可实现的选择。

核心方法与参考资料都在本目录内，不需要作者的私人规则、素材库或聊天历史。设计理念以Apple设计知识为主要参考，同时吸收其他设计方法；它不是Apple官方作品，也不代表所有平台已完成实测。

## 安装与开始使用

下载整个目录，文件夹命名为`interface-design`，保留`SKILL.md`、`references/`和其他随包目录的相对位置。不要只复制`SKILL.md`。

公开仓库：[nate-ai-skills](https://github.com/nate2022-ai/nate-ai-skills)。本Skill位于`skills/interface-design`，可单独安装。可直接把下面这段交给Codex：

```text
请使用 $skill-installer 从 https://github.com/nate2022-ai/nate-ai-skills
安装 skills/interface-design 的完整目录，并确认能够发现 $interface-design。
若已安装，先核对我的本地定制，再按我确认的范围更新。
```

在Codex中，可以将目录放在：

- `~/.agents/skills/interface-design/`：个人使用。
- 你的项目的`.agents/skills/interface-design/`：只在该项目使用。

安装后可直接说“使用 $interface-design ……”或描述相应界面任务。Codex通常自动发现新增Skill；未显示时可重启。也可让可用的`$skill-installer`从实际GitHub仓库链接安装。安装位置、自动发现与插件分发以[Codex官方说明](https://learn.chatgpt.com/docs/build-skills)为准；面向Codex的集中分发还可按其说明增加插件包装。

其他支持[Agent Skills格式](https://agentskills.io/specification)的工具，按各自的安装位置和调用方式配置。`agents/openai.yaml`是Codex显示与默认提示配置，其他工具可按需要适配；本包没有逐一验证所有客户端。没有原生Skill功能时，也可把`SKILL.md`交给能读取同目录参考文件的AI，但这不等于该工具已经支持自动发现。

## 使用示例

> 使用 $interface-design，帮我审查当前页面的信息主次和操作反馈，先给问题与建议。

> 给这个手机表单做一个更容易填写的方案，先展示主要布局和错误状态。

> 到设计奖和获奖网站找与这个数据工作台相似的案例，打开相关界面，说明借鉴什么、怎样适配，不只给链接。

> 参考优秀电商网站改进商品浏览。保留现有业务逻辑，按项目已确认的范围落实。

提供目标、实际内容或现有代码、平台及关键限制即可；缺少会影响方案的信息时，AI再定向询问。只需要审查或参考时，不自动修改项目。

## 工具条件与按习惯适配

| 要做的事 | 需要的条件 |
|---|---|
| 设计判断、文字方案 | AI能读取本包；有必要的任务和项目材料 |
| 检索设计奖或核当前规范 | 可用的网页搜索或浏览能力；不绑定某个搜索商或API |
| 评价视觉与交互 | 看图、浏览器、视频或目标设备等与证据匹配的能力 |
| 实现与运行验收 | 目标项目的编辑、构建、运行工具；原生或设备相关能力由使用者提供 |

没有联网能力时仍可使用包内方法，但不能核查最新案例；没有视觉或运行工具时，交付应说明只完成文字/源码检查。基础使用没有Python、Node、API Key或其他Skill的硬依赖。`scripts/check_package.py`仅供维护者检查文件，需要Python 3.9或更新版本。

可以按自己的习惯选择AI工具、浏览器、输出语言、技术栈、设计系统、交付形式、草稿确认方式、案例保存位置与验收范围。建议把项目偏好写在所在项目支持的规则文件（例如`AGENTS.md`）或本次请求中；确实要改通用方法时，再维护自己的Skill分支。不要把凭证、客户资料和私人规则一起上传公共仓库。

研究过程也随包提供，供想理解来源和取舍的人阅读，不要求使用前通读。项目的研究、收藏与反馈可留在自己的现有位置，无须搭建作者同款资料库。按实际目标做相称验证即可，不要求使用者先适配所有平台。

## 目录与文件夹作用

普通使用者先看这份README完成安装，再把任务交给AI。AI从`SKILL.md`进入，遇到具体问题才读取对应参考。整包保留，按需阅读；无需先理解每个文件才能使用。

```text
interface-design/
├── README.md               给使用者看的安装、用法和目录说明
├── SKILL.md                给AI执行任务的主入口
├── LICENSE                 本Skill的MIT使用许可
├── agents/                 Codex中的显示与默认调用配置
│   └── openai.yaml
├── references/             按设计问题读取的现行方法与来源说明
│   ├── visual-system.md
│   ├── information-patterns.md
│   ├── platforms.md
│   ├── interaction-motion.md
│   ├── user-control.md
│   ├── evaluation.md
│   ├── design-case-research.md
│   └── sources.md
├── research/               经过脱敏的研究经过与历史来源记录
│   ├── design-method-evolution.md
│   └── apple-hig-reading-map.md
└── scripts/                维护与分发时使用的文件检查工具
    └── check_package.py
```

### agents：让Codex正确显示这个Skill

[agents/openai.yaml](agents/openai.yaml)保存中文显示名称、简短介绍和默认调用提示。它影响使用者在支持该配置的界面里看到的名称与提示；设计任务怎样执行仍由`SKILL.md`和参考资料说明。目录名`agents`不表示这里配置了一支多代理团队。

正常安装后通常无需修改。想调整显示名称或默认开场提示，可以在自己的安装副本中修改这些字段；改用其他AI工具时，按该工具的配置格式适配。安装时保留Skill目录名和运行名`interface-design`；中文显示名可以按需调整，介绍和提示应与实际能力一致。

### references：解决当前设计问题的方法

这里保存可以直接指导当前任务的专题参考。AI根据`SKILL.md`中的路由选择相关部分，使用者也可以按下表查阅。每篇解决的重点不同：

| 文件 | 主要作用 | 什么时候用 |
|---|---|---|
| [visual-system.md](references/visual-system.md) | 整体视觉、排版、中文与数字、色彩、图像、材质、组件一致性、界面文字与品牌语气 | 页面重点不清、密度不合适、风格不统一，或需要建立视觉方向时 |
| [information-patterns.md](references/information-patterns.md) | 导航、对象查找、搜索筛选、表单、批量操作、表格图表及复杂状态的信息组织 | 决定哪些内容放一起、用表还是卡片、如何选择和比较对象时 |
| [platforms.md](references/platforms.md) | 不同窗口、输入方式和平台的布局与任务连续性，及专用宿主条件 | 从桌面适配手机、调整窗口，或转到原生、小程序等平台时 |
| [interaction-motion.md](references/interaction-motion.md) | 操作反馈、动效、弹层、焦点、手势、媒体与可中断性 | 用户不知道是否操作成功、弹层难退出、动画打断任务或输入方式有差异时 |
| [user-control.md](references/user-control.md) | 通知、权限、账号、分享协作、跨设备状态与系统外部入口 | 设计访问权限、账号结束、共享对象、同步状态或通知后的返回路径时 |
| [evaluation.md](references/evaluation.md) | 界面审查、原型试验、端到端验收、无障碍、性能及证据范围 | 检查方案能否实际完成任务，或判断哪些结果已验证、哪些仍待验证时 |
| [design-case-research.md](references/design-case-research.md) | 设计奖与优秀作品的检索入口、奖项身份核查、实际观察和适配方法 | 想找类似界面、借鉴获奖网站，或为设计选择寻找具体参考时 |
| [sources.md](references/sources.md) | 知识和上游方法的出处、采用范围、许可线索及冲突处理 | 想追溯依据、判断某条规范是否适用，或维护和扩展Skill时 |

例如“数据工作台在手机上比较困难”，可以结合信息模式与平台适配；“找获奖案例帮助改进这个工作台”，再使用案例检索。所需资料由当前问题决定，不要求每次把八篇全部读完。

### research：理解方法是怎样形成的

| 文件 | 记录什么 | 阅读用途 |
|---|---|---|
| [design-method-evolution.md](research/design-method-evolution.md) | 目标与来源如何确定、研究中的修正、方法怎样进入Skill，以及验证范围 | 理解为什么采用这些方法，或继续研究、维护自己的版本 |
| [apple-hig-reading-map.md](research/apple-hig-reading-map.md) | 2026-09-20的Apple HIG来源快照：173个节点的公开链接、当时状态和阅读深度 | 找回原始官方入口，了解历史研究覆盖了什么、哪里仍需深化 |

这些是可公开的研究摘要与历史记录，不包含完整私有对话或Apple全文。历史“已读”也不代表网页内容至今没变。当前任务的执行方式以`SKILL.md`及相应参考为准；研究中出现的候选和未验证结论保留其原状态。

普通使用无需修改研究档案。想补充自己的研究，可以记录新的日期、来源、适用条件与验证结果；要让研究结论成为自己的执行方法，应明确更新对应的主入口或参考文件，避免只在历史记录里暗中改变默认行为。

### scripts：检查改动后的包是否完整

目前只有[check_package.py](scripts/check_package.py)，用于检查必需文件、主入口的基础字段、本地链接和标题锚点，以及越出包目录的引用、机器路径和软链接。维护者在调整文件或准备分发后，可以在Skill目录运行：

```bash
python3 scripts/check_package.py
```

这个检查工具需要Python 3.9或更新版本，不需要额外Python包。普通使用Skill无需运行它，也无需因此安装Python。它不会评价设计好坏、证明所有外部网站可用或识别全部敏感信息。设计奖案例检索由AI按专题方法调用已有搜索/浏览工具完成，这里没有后台爬虫或持续运行服务。

### 主要文件怎样配合，个人习惯放哪里

`README.md`帮助人安装与理解，`SKILL.md`说明AI怎样开展任务，`references/`补充相关方法，`research/`解释这些方法的研究背景，`agents/`适配客户端显示，`scripts/`帮助维护者检查文件结构。

配色、语言、技术栈、交付方式和案例保存位置等项目偏好，优先写进当前请求或项目规则。需要改变通用方法时，再修改自己的Skill版本；调整文件名或位置后同步更新相关引用，安装和更新时仍以完整目录为单位。

## 完整性与发布状态

在本目录运行`python3 scripts/check_package.py`，检查必需文件、包内链接、越界引用和软链接等结构问题。它不会验证每个网络链接、识别全部敏感内容或证明设计质量。维护者发布前还应审阅文件内容；安装者按自己的工具和目标任务试用即可。

本目录包含可独立安装的完整知识包，具体实测范围见[研究与验证边界](research/design-method-evolution.md#验证边界)。并未承诺全离线实现、所有AI客户端或所有设备均已验证。

本包沿用公开仓库的[MIT License](LICENSE)，完整许可随Skill一起提供，方便独立安装和再分发。第三方规范、案例、图片、字体、代码和商标遵守各自条款；来源链接和奖项身份不授予素材转载权。包内提供自主整理与公开来源导航，不捆绑第三方完整网页、图片、视频或字体。
