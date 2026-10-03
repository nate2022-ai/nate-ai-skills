# 来源、转化与使用边界

本篇用于追溯、冲突处理和维护；普通任务按问题展开。首版编制日期2026-09-20，正文为中文整合与项目选择；来源原文、适配方法、参数选择、实际验证结果分开理解。方法进入Skill不等于所有平台已验证。

## 为什么这样组织

保留本项目“设计/审查/改造/验收”四种任务路由，以Impeccable按用户成功方式理解界面的做法补强核心；frontend-design帮助建立有意图的视觉表达，Emil补交互因果与动效，Pro Max补按问题查询，Vercel补可定位检查，旧business-ui-design保留有效的业务模式与运行验收。

Apple是系统知识母本；成熟Skill帮助把知识变成AI工作方法；目标平台资料负责具体实现条件；真实应用负责检验本地选择。关注度用于优先研究，不作为每条方法正确或当前项目适用的证明。

## Apple官方：当前知识与来源覆盖

2026-09-20首版最初核读11个主题的部分内容，同日分批扩展。下列为累计状态；历史逐页状态见随包研究记录。

- 官方HIG根目录的`topicSections`递归定位173页，含15个目录页和158个内容页；累计157篇内容有正文或相关段落阅读记录，深度逐页标记。余下1篇VoiceOver未在该轮继续深入；这是当时的研究边界，不限制其他使用者的专项任务。长篇按相关章节选择读取，不据页面覆盖宣称全部细节已理解。
- 覆盖原则、视觉、文字、无障碍、导航、图表、输入、交互、平台适配、通知、权限、账号、共享、媒体、智能建议、空间/AR与系统生命周期。HIG外另定位Design Pathway、Resources、Fonts、SF Symbols、Design Videos、Design Awards、What's New七类入口，抽读六篇代表文字材料；未看完全部视频、案例或资源包。
- 专题内容是有出处的自主归纳与跨平台适配，不是官方全文译本。已核方法不等于原生API、真机或业务效果已验证。

公开包随附[Apple逐页来源阅读记录](../research/apple-hig-reading-map.md)和[设计方法研究过程](../research/design-method-evolution.md)。它们保留历史研究范围、公开出处、读取深度和方法演化，已移除私人资料库位置、内部身份信息与运行回执。核心方法和专题资料均可直接从本包读取，普通任务无需先读全部来源目录。

| 方法问题 | 已转化的位置 | 继续使用的条件 |
|---|---|---|
| 品牌、排版、中文、主题、图像、图标与材质 | [视觉与设计系统](visual-system.md) | 字体/图标/模板许可与目标平台资源独立核查 |
| 搜索录入、控件、图表、帮助、设置、生成式结果与预测纠错 | [信息模式](information-patterns.md) | 真实指标、数据类型、权限和接口能力仍由项目确定 |
| 焦点、临时容器、拖放、进度、撤销与媒体会话 | [交互](interaction-motion.md) | 关闭、草稿与正式提交不可混并，恢复必须真实可用 |
| 多窗口、分栏、空间/AR、腕上/电视及宿主生命周期 | [跨平台](platforms.md) | 原生系统能力不直接映射Web/Android/小程序 |
| 通知、权限、账号、多人协作与系统外部入口 | [用户控制](user-control.md) | 实际产品流程与发布要求按目标环境核实 |
| 研究原型、辅助输入、多感官与RTL | [验证](evaluation.md) | 静态推演、辅助技术实测和业务体验分别留证 |

### 原文与资源留存边界

本次正式入库的是自主研究、来源目录与方法位置；**没有把官方全文、配图、视频、字体或UI Kits复制入正式库**。研究临时读取使用Apple公开页面及同站正文JSON，后者的文本提取会遗漏分栏/页签结构，因此对采用的相关内容补查原始结构与表格，不能将提取文本声称为整页视觉内容。

Apple[网站条款](https://www.apple.com/legal/internet-services/terms/site.html)包含复制与分发限制，公开可读不能据此推定存在业务资料库整库复制许可。使用者按自身资料管理方式保留有权留存的内容；未确认全文留存条件的，保留准确官方入口与自主整理，不伪报原文已存。具体素材各有用途和条款，不随Skill重新分发。

### 仍未覆盖什么

当前HIG目录快照中需要处理的“仅定位”内容页已完成相关正文核读，但部分长页的完整规格、所有配图和动态演示、下级实现文档、完整历年视频与案例仍未全覆盖。健康、支付、车载等已建立方法摘要与官方入口，具体实现按实际产品范围深化。此前研究未完成无障碍与本地化专项验收，已有资料保留；使用者按实际任务确定专项范围。Android、Web和小程序自身的规范不能由Apple资料替代。文件覆盖、方法理解和运行效果分别评价，范围完整性不由页面计数单独证明。

## 成熟Skill：直接借鉴什么

以下固定链接对应本轮核对版本；不是要求普通调用每次联网刷新。中文正文按本项目条件独立组织，未整篇复制上游正文或执行脚本。

| 来源 | 核读范围 | 吸收与取舍 |
|---|---|---|
| [frontend-design](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/SKILL.md) | 正文全文 | 从内容/目的形成视觉方向；不继承对特定字体和风格的普遍禁令 |
| [Impeccable](https://github.com/pbakaus/impeccable/blob/f2c7051853848826aac2f4646581d62a732155ad/.agents/skills/impeccable/SKILL.md) | 入口、operate、adapt、adapt.native全文；critique前209行；craft-floor部分标题和相关行 | 任务成功方式、上下文、整体审查与跨平台适配；不复制命令体系、固定代理编排或评分流程 |
| [Emil design-eng](https://github.com/emilkowalski/skills/blob/85e8e2363b713506e1d5b6e07a0eb2da66be1bc3/skills/emil-design-eng/SKILL.md) | 前310行，另结合此前相关研究 | 动效目的、频率、因果和连续性；不继承按钮必须缩放、键盘永不动画等绝对要求 |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/de5f12b400775997d213524ef02a7c7d2746806f/.claude/skills/ui-ux-pro-max/SKILL.md) | 需求、查询、工作流和无结果处理，至145行；配套沿旧研究 | 围绕问题和技术栈找方法、核匹配；不照搬固定领域优先级或安装工具链 |
| [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | 此前入口和规则研究，另核仓库Web检查范围 | 发现应可定位并能帮助修复；代码扫描不代替运行观察 |
| 此前维护的业务界面设计方法 | 核心全文及相关专题 | 四种任务、业务数据/表单/反馈、真实环境验收；取消逐条五关门槛与旧组件天然优先的继承 |

许可核对：Anthropic frontend-design与Impeccable对应版本标为Apache-2.0，Emil及Pro Max标为MIT；Vercel许可本轮未核。不因链接或方法参考声称重新授权上游文件；后续若直接复制/改编上游正文、代码或资产，须保留相应许可、署名及适用变更说明。许可原文：[Anthropic](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/frontend-design/LICENSE.txt)、[Impeccable](https://github.com/pbakaus/impeccable/blob/f2c7051853848826aac2f4646581d62a732155ad/LICENSE)、[Emil](https://github.com/emilkowalski/skills/blob/85e8e2363b713506e1d5b6e07a0eb2da66be1bc3/LICENSE)、[Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/de5f12b400775997d213524ef02a7c7d2746806f/LICENSE)。

## 平台与标准补充

本轮直接读取：
- [Android自适应](https://developer.android.com/develop/ui/compose/layouts/adaptive/get-started-with-adaptive-apps)：按窗口/姿态组织区域、状态连续及多输入；未执行Android代码。
- [W3C Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)：重排和二维内容例外。
- [W3C Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)、[Contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)、[Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)：相应条款及条件。
- [MDN dialog](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role)：语义、名称、焦点及操作责任。

W3C Understanding为条款解释；涉及正式符合性结论时回到规范文本与完整相关条件。小程序各宿主、非Apple桌面系统及平台专项API尚需按任务查具体官方资料；它们已进入能力组织，不冒称已建立全部专项知识或运行验证。

## 冲突、缺口与参数如何处理

先看用户有效目标、事实和授权，再核规范是否真的适用当前平台与条件。可靠约束保持明确；专家偏好、示例值和本地选择有适用条件。若做法互相冲突，解释各自解决什么问题，在当前任务中比较结果和成本，保留影响选择的理由；不能简单按Apple、Star或“项目已有”排序代替判断。

原文强语气不自动成为跨平台硬要求。转化时讲清目的、条件、系统/作者各自责任和有效替代，但不把所有方法弱化成“随便选”。普通可靠方法可直接形成候选方案；重大未知用最低成本且在授权内的试验解决，依赖用户独有决定才提问。

设计方法、公开来源索引和脱敏研究与Skill同包；使用者新增研究沿自己的项目或资料库保存，应用结果归原项目。当前来源索引与已读记录不等于官方原文已入库。来源完整性、能力内容覆盖与效果验证分别标记；文件数、检索命中和原文数量都不能独自证明能力完整。

## 设计奖与优秀案例

按任务调用[设计案例检索](design-case-research.md)，覆盖Apple Design Awards、Awwwards、CSS Design Awards、UX Design Awards与Red Dot。来源身份、当前可访问内容、实际观察与项目适配分别判断；获奖不是可用性或商业效果的通行证明。2026-10-03核查中部分网站目录页读取受限，具体案例可访问；不把入口存在写成随时可用的API能力。

## 研究演化与公开使用

跨平台目标、完整首版整合、按需知识、代表性检验及范围纠偏见[研究过程](../research/design-method-evolution.md)。私人研究记录保留原始证据，公开包提供已脱敏的可复用经过，不要求使用者获得作者的私人资料库。

安装者可以按所在项目的规则、工具与习惯调整草稿确认、存放位置、实现与验证方式，见[README](../README.md)。当前包是完整方法入口，来源和历史阅读数量不代替实际使用效果；未验证的平台与行为继续如实标注。
