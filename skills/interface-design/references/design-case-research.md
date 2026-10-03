# 设计奖与相似案例检索

用户要参考设计奖、获奖网站、同类产品，或方案需要外部例子帮助判断时读取。目标是找到可解释、可迁移的设计方法，并用当前项目的内容与条件作出选择。使用当前环境已有的网页搜索、浏览、看图能力；不依赖私人资料库、其他 Skill、固定浏览器、付费账户或假定存在的 API。

## 从问题选择来源

先明确平台、使用者、核心任务和待解决的问题，例如“手机逐步操作”“桌面多对象比较”“电商商品发现”。相似性优先看任务、信息关系、交互与输入条件，再看行业和视觉风格。用户已提供这些条件时直接使用，不重复访谈。

| 来源与入口 | 适合寻找什么 | 需要分清什么 |
|---|---|---|
| [Apple Design Awards](https://developer.apple.com/design/awards/)；[2024获奖与入围页](https://developer.apple.com/design/awards/2024/) | 原生应用、操作连续性、平台输入、信息层级 | 绑定年份与类别区分 Winner 和 Finalist；应用奖与网页奖不同 |
| [Awwwards](https://www.awwwards.com/websites/) | 品牌站、电商、作品集、网页构图与动效；也可从 Elements 查局部界面 | 按具体页保留 Site of the Day、Honorable Mention 等身份；Nominee、灵感收录、推广条目不能统称获奖 |
| [CSS Design Awards 获奖列表](https://cssdesignawards.com/wotd-award-winners)；[评奖说明](https://cssdesignawards.com/about) | 网页表现、导航、UI、UX和创新交互 | WOTD、WOTM、WOTY、Special Kudos与公众UI/UX/Innovation奖分别记录，正在评分不等于获奖 |
| [UX Design Awards](https://ux-design-awards.com/winners) | 数字产品、业务工具、复杂流程与体验研究 | 页面路径含 winners 不足以判奖；核具体年度、类别与奖项标记，区分产品、概念及入围 |
| [Red Dot](https://www.red-dot.org/)；[界面案例DXA](https://www.red-dot.org/project/dxa-digital-experience-audit-55219) | 产品界面、数字服务、信息组织与品牌沟通 | 核对应奖项体系、年份和类别；公司得奖不代表其每个产品都得奖 |

按当前问题挑合适的入口，已有足够匹配证据就停止，不逐站穷举。业务工具可以优先查UX Design Awards或Red Dot的界面作品；品牌网站可以先看Awwwards或CSSDA。其他有可靠出处的优秀设计也可使用，准确写“产品参考”或“灵感案例”，无需硬找奖项。

## 查询、核实与观察

1. 用任务关键词与界面问题组合搜索，可中英互换、替换同义词。例如下列是查询样式，不代表对应结果已找到：
   - `site:awwwards.com/sites/ ecommerce navigation`
   - `site:cssdesignawards.com/sites/ product storytelling`
   - `site:ux-design-awards.com/winners dashboard analytics`
   - `site:red-dot.org/project interface workflow`
   - `site:developer.apple.com/design/awards/ Interaction recipe`
2. 打开少量相关官方案例页，核作品名、设计方、年份、准确奖项身份和与任务有关的说明。保留官方身份原词与授予范围；Winner、Finalist、Nominee/nominated分别表述为获奖、入围、提名，不合并成同一种荣誉。搜索摘要用于发现，不能代替详情核实；只有摘要证据时说明身份待正文核实。获奖身份、作者主张和我们观察到的事实分开表达。
3. 看与问题相关的真实材料：官方截图、演示、原网站、产品页或应用商店页面。视觉结论应基于实际看到的图或页面；交互结论优先来自实际操作或明确展示该行为的演示。只读到文字时说明“页面描述，未看图/未操作”，不要声称已观察布局或验证交互。
4. 区分评奖时版本与当前版本。当前原站可能已改版、关闭或转为营销页；不能用当前截图证明历史获奖版本，营销展示也不证明后台任务已经可用。
5. 从观察中提炼可借鉴的方法，例如对齐比较、分组方式、逐步指引、反馈位置或总览到详情的连续性。说明当前项目怎么采用、需要调整什么，再在原授权内进入草稿或实现。案例借鉴不授权照搬代码、品牌外观或业务结论。

无法访问时可换用同一作品的官方介绍、设计方材料或其他案例，并准确标注来源与未核项。登录、付费或验证限制不绕过，不反复重试无变化的阻碍。没有联网能力时，使用用户给出的资料或明确标为历史的随包例子，说明无法核当前信息；查到名称不等于完成案例研究。

## 返回可用于决策的结果

给出足以支撑选择的少量案例，不凑固定数量。可以用紧凑表格或逐项说明：

- 作品与官方链接；核到的奖项、年份、类别、准确身份。
- 与当前任务相似的具体信息或操作，实际观察了哪张图、哪个区域或哪段流程。
- 值得采用的方法、在本项目的适配方式，以及不能直接搬用之处。
- 证据范围与核查日期：文字、图像、演示和真实操作分别标明。

最后推荐适用的方法组合及理由，而非把选择全交回用户。获奖只说明评奖结果，不能替代本项目的内容、输入方式、性能、可访问性与业务验证。作者公布的效果数字注明出处和条件，不能当成本项目收益预测。

## 历史研究示例

下面是来源发现与方法提炼的例子，不是默认设计配方。2026-10-02原研究记录曾直接看官方图；2026-10-03本次编制复核官方案例文字页。再次用于视觉判断时应重新打开所需图片或现行页面。官方素材以链接提供，不随包分发。

| 作品与身份 | 研究观察与可迁移问题 | 限制 |
|---|---|---|
| [E2E Analytics](https://www.awwwards.com/sites/e2e-analytics)，Awwwards Honorable Mention，2023-06-23；[Dashboard元素](https://www.awwwards.com/inspiration/dashboard-e2e-analytics) | 原图按分析、增长、受众分组，入口配小图；可研究如何使功能分组与用途一致 | 展示图含占位文字，没有明细表操作证据；链接所指的开发案例展示不等于可用后台 |
| [Uno](https://ux-design-awards.com/winners/2025-1-uno)，UX Design Awards 2025 Spring，Product，页面有评审评价与获奖段落 | 原图中回答附Sources入口；可研究如何让摘要、依据与当前对象就近出现 | 未使用真实产品；页面宣传的效率、查询与定制能力不直接迁入当前项目 |
| [DXA Digital Experience Audit](https://www.red-dot.org/project/dxa-digital-experience-audit-55219)，Red Dot Brands & Communication Design 2021，User Interface | 原图分总览、问题、结果和详情；可研究整体判断与按需查证的关系 | 静态图不证明筛选、悬停或动效可用；抽象评分和图表不能替项目定义指标 |

Apple身份核对示例：[2024年度页](https://developer.apple.com/design/awards/2024/)的Interaction类别中，Crouton位于Winners，Arc Search位于Finalists。这只是年份/类别/身份的辨别例子，不表示二者适合所有移动任务。

研究记录可按使用者习惯保存在项目、书签或案例库中。只有用户要求持续收藏或监控时才按相应授权处理；普通查找不自动建立数据库、订阅、抓取器或后台任务。
