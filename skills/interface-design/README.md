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

## 包内导航

- [SKILL.md](SKILL.md)：AI执行入口与按问题读取路由。
- [视觉与设计系统](references/visual-system.md)、[信息模式](references/information-patterns.md)、[跨平台](references/platforms.md)、[交互动效](references/interaction-motion.md)、[用户控制](references/user-control.md)、[验证](references/evaluation.md)。
- [设计案例检索](references/design-case-research.md)：设计奖入口、检索方法、案例判断与历史例子。
- [来源与边界](references/sources.md)：上游来源、采用范围与未覆盖内容。
- [研究过程](research/design-method-evolution.md)、[Apple来源阅读记录](research/apple-hig-reading-map.md)：公开整理的研究经过与历史来源状态。

## 完整性与发布状态

在本目录运行`python3 scripts/check_package.py`，检查必需文件、包内链接、越界引用和软链接等结构问题。它不会验证每个网络链接、识别全部敏感内容或证明设计质量。维护者发布前还应审阅文件内容；安装者按自己的工具和目标任务试用即可。

本目录包含可独立安装的完整知识包，具体实测范围见[研究与验证边界](research/design-method-evolution.md#验证边界)。并未承诺全离线实现、所有AI客户端或所有设备均已验证。

本包沿用公开仓库的[MIT License](LICENSE)，完整许可随Skill一起提供，方便独立安装和再分发。第三方规范、案例、图片、字体、代码和商标遵守各自条款；来源链接和奖项身份不授予素材转载权。包内提供自主整理与公开来源导航，不捆绑第三方完整网页、图片、视频或字体。
