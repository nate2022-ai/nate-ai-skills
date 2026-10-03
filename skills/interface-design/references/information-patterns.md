# 信息组织与界面模式

适用：内容组织、导航、检索、录入、数据阅读与复杂状态。各模式按任务组合，不是每页必备模块。直接继承旧Skill有效业务方法，并取消固定页面配方；依据见[sources](sources.md)。

## 导航与空间

导航表达“在哪、能去哪、如何回来”，操作表达“对什么做什么”，筛选表达“看哪些内容”。不要把三种语义都伪装成同样的页签。全局与局部导航建立明确层级；只有一个层级时无需多套栏。

根据可用空间和任务选择底部导航、侧栏、页签、菜单、列表到详情或多窗格。高频访问与低发现性内容需要更直接的入口；二级选项按需展开时，主入口的名称要能预测里面有什么。不要仅为减少首屏高度收起所有工具。

搜索、筛选、阅读位置和未保存输入应在合理返回路径保留。链接、页面跳转和弹层关闭按平台约定工作。草稿将影响体验的全局壳一并展示，局部组件试验可限定上下文。

## 查找与对象选择

查找或选择类工作台优先沿使用者认识对象的顺序进入，再在需要处展开型号、颜色、供方或其他条件。用户给出的高频例子可作捷径，不当作完整目录；捷径保留归属，分类外项目仍可通过全部内容与原名搜索找到。浏览分组不直接成为数据的正式身份。

分类或型号的选择可以用卡片，价格与共同属性的比较保持行列关系。不要按页面第几级机械规定图片、卡片或列表。若整个结果都缺少某个不影响当前判断的辅助字段，可省去空列；关键口径未知仍须可辨认，原值保留在证据处，不填0或删数据来凑整齐。

首屏呈现当前判断所需信息，历史、解释和原始证据在需要时展开。当前任务就是趋势分析时让图表主导；查单个对象价格时，历史小图可以放在展开后。布局或图表随窗口重排时，尽量保留搜索、选择、已展开证据和阅读位置，避免只为调整图尺寸重建整页。

## 搜索、筛选与内容选择

明确搜索范围与匹配对象；用户按编码精确找对象时展示编码和匹配关系，视觉探索时给图像更多空间。标签、别名和语义拓展不能混成同一种精确匹配承诺。

当前条件、结果数量或范围在有助理解时呈现；不是所有入口都必须显示总数。无结果提供与原因对应的清除或调整方式。切频道时明确保留哪些查询和条件，“全部”究竟指全部频道还是清空所有筛选，文案与行为一致。

多个二级入口应对应真实可区分的任务或结果；数据暂未支持时不以假分类误导。自动加载防止较早请求覆盖较新的选择；返回时核状态与结果一致。

批量操作说明已选对象及范围，区分当前页、跨页和全量。完成反馈区分成功、明确失败、结果待核对和未提交项；部分失败保留可恢复路径。结果不明时沿[分阶段完成](user-control.md#跨设备状态与分阶段完成)核实际状态，不把未知项并入失败重试。不同权限不允许以隐藏按钮代替后端授权。

## 表单与编辑

按用户的思考或操作顺序组织字段，标签使用能理解的业务语言，必要单位、格式示例与错误靠近相关字段。默认值确实适用才预填；区分只读、自动计算、可选和必填。

验证时机兼顾即时纠错和输入中的正常中间态，避免每敲一个字符都报错。提交失败保留已填信息，说明影响和可修正原因；长流程考虑草稿或分步，但不能把一个简单表单拆得更费力。

自动保存、显式提交、撤销和并发冲突是不同语义。展示的是“正在保存”“已保存”“失败待重试”还是“本地草稿”，应对应真实状态；权限、审核和正式统计状态不因视觉简化混并。

破坏性动作按后果选择预览、撤销、确认等保护，不能承诺后端不存在的恢复能力；普通可逆操作无需重复确认。

## 表格、列表与数据关系

选择形态看阅读任务：跨对象比较相同指标适合保持行列关系；逐条读丰富内容可以列表或卡片；图像探索可以网格。二维关系必要时保留表格及局部滚动，标题、筛选和说明仍按空间重排。

身份、单位、日期、比较基准和关键状态出现在需要判断的位置。排序按实际数据含义；对齐服务比较；数值0、缺失、未知、尚未采集、失败应可区分。不要为排版用0补缺值，也不从缺基准计算增长率。

固定列、表头、虚拟滚动和分页按实际内容规模选用，检查键盘顺序、读屏关联和查找方式。长名称、负数、大数、多个单位及极端状态不能只用理想数据绕开。

指标卡是否必要看它能帮助什么判断。图表按问题选：趋势看时间关系，排名看大小，组成看占比及总量。保留单位、时间范围和不可比较条件；不要用截断坐标或面积变化无意放大差异。交互图表的关键信息需要可获得的文字或数据替代。

## 状态与反馈作为流程的一部分

- 首次无数据：解释如何开始；筛选无结果：调整查询；失败：重试或恢复；未同步：说明新鲜度；无权限：给适当说明。它们不是同一空状态。
- 等待期间保留仍可信的上下文，局部更新不必遮住全部内容。旧结果可保留但注明正在更新，避免误认新条件结果。进度未知不伪造百分比。
- 网络断开、超时、重复点击、过期结果和部分成功按实际架构处理；不在前端承诺接口不具备的幂等性或离线能力。
- 主操作反馈及时，后续变化尽量保持阅读位置。完成后给实际结果与下一步，不靠一闪而过的提示承担所有证据。

## 场景转换的例子

素材检索页面可把方向入口收紧，二级细项按需展开；经营日报的异常与比较基准可能需要直接呈现。二者共享层级和状态方法，不共享固定首屏配方。

手机逐条审核时可以聚焦当前对象；桌面批量对照时可并列列表与详情。任务改变，布局可以改变；对象、字段、选中与审核含义不能随之漂移。以上为方法示例，不作为已验证优秀样本。


## 按选择含义挑控件

先判断选的是一个值、多个对象、持续状态，还是执行动作，再考虑外观与占用空间。

| 需要表达的选择 | 常见起点 | 需要改变方案的条件 |
|---|---|---|
| 两个相反状态 | 开关、复选框或可切换按钮 | 分清当前状态与点击后动作 |
| 多个对象与批量选择 | 支持多选的列表与复选框 | 父级在部分子项选中时显示混合状态，并说明点击后的选择范围；不要用普通两态开关冒充部分选中 |
| 少量互斥选项 | 单选组或分段控件 | 标签太长、无法并列比较时，改为菜单或列表；选项数不是跨平台固定上限 |
| 一组紧密相关的视图/属性 | 分段控件 | 不把执行动作与持续选中混在同一组；跨大模块导航另选导航组件 |
| 较多且有顺序的值 | 选择器、菜单或可检索列表 | 按选项规模、熟悉度及定位速度选择；不要求用户在很长滚轮中找商品 |
| 连续调节或大致试探 | 滑块 | 需要精确数值时给可输入值；小步增减可配步进器，边界和步长可理解 |
| 日期、数量与编码 | 对应的输入/选择方式 | 数量可计算，编码可能含前导零；显示格式、本地化和实际数据类型分别处理 |

菜单按任务关系分组；频率决定组的优先位置，但低频关联命令不必因此拆散。可展开菜单中的不可用项是否保留，取决于发现需求和当前上下文；权限信息不因暴露命令名而泄露。图标、英文大小写和控件数量建议不能直接变成中文全平台规范。

依据：[Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles)、[Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)、[Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers)、[Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders)、[Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers)、[Menus](https://developer.apple.com/design/human-interface-guidelines/menus)。数据类型例子是本项目适配。

## 把图表的比较条件做清楚

先说明读者要发现趋势、比较大小还是查具体值；只需逐条查数时，表格可能更直接。概览与详情保留系列名称、单位和编码关系，不能切视图后让同色代表另一对象。

柱长承担大小比较时，零基线通常关键；折线强调某区间变化时可使用非零下界，但应清楚显示范围。多图并排比较时检查尺度是否一致；自动缩放后提示变化，避免把同样的视觉起伏误看成同等幅度。电量、完成比例等有自然边界的指标需保持边界含义；增长率可能超过100%或为负，不能仅因单位为百分比就固定在0–100%。

图表标题和简短结论帮助入门，但不替代数据。重要事实不只藏在悬停提示中。可交互的小点应有更容易命中的区域与键盘路径；大量点可以按有意义的组访问，不强迫读屏逐点遍历。提供对象、时间、值与单位，避免只读“红色线”。原生Swift Charts的默认辅助能力不能当作Web图表已经具备。

例：店铺日报的柱图用于比较当天出库量，折线用于观察各店变化；没有采集的日子标缺失，不连成“零出库”的趋势。是否以共同尺度展示，取决于比较绝对量还是各店自身波动。这是业务适配示例，未用它替代真实指标定义。

依据：[Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data)、[Charts](https://developer.apple.com/design/human-interface-guidelines/charts)。

## 搜索与录入的条件化取舍

全局查找与当前列表过滤可以并存，但各自范围要清楚。按输入即时查找适合反馈快、开销可控的查询；成本高或输入尚未完成时可以提交后查询。中文输入法合成、快速连续输入与较早请求晚返回需单独处理；这是Web实现适配，不是Apple规定的搜索时序。历史查询涉及共享设备或敏感内容时，考虑关闭或清除入口。

从现有事实预填可以减少劳动，但不能为了少填一个字段而额外索取无关权限。错误提示的时机兼顾用户正在输入的中间状态；禁用提交若让人找不到原因，可用字段说明或提交时定位错误。显示格式不是数据校验，更不能用数字格式化破坏款号、邮编等标识。

依据：[Searching](https://developer.apple.com/design/human-interface-guidelines/searching)、[Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)、[Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)、[Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)。

## 首次使用、帮助与设置

让人尽早完成一个真实小任务。必要前置条件解释其作用；可后补的偏好不挡主流程。引导适合贴近当前动作，用过的人可跳过，之后仍能找到；涉及真实数据的教学不能伪装成无影响练习。

简单疑问在附近解释，复杂任务给完整步骤；提示是否出现取决于当前任务和是否已掌握，不继承固定“每天一次”或“三步以内”的通用限制。关键警告与操作不能只存在于短暂提示或鼠标悬停中。

把本次任务的筛选、排序、显示范围放在任务现场；跨任务的低频偏好进入设置。采用合理默认，尊重系统文字和辅助设置；仅在确有用途且范围清楚时提供应用自身覆盖项。

依据：[Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)、[Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help)、[Settings](https://developer.apple.com/design/human-interface-guidelines/settings)。

## 生成式功能的结果与控制权

界面明确区分生成建议、已核事实和已执行结果。给出贴近任务的输入例子；生成后提供适用的编辑、重试、比较或撤销入口。等待提示对应真实阶段，不伪造推理过程或百分比。AI是辅助功能时，失败或不启用后尽量保留基本任务；不可替代的核心能力说明不可用原因。

对会改变业务数据或难以撤回的动作，按已有授权和实际影响展示对象与结果再执行；不把生成草稿当作正式提交，也不因此要求所有普通可逆操作重复确认。数据发送范围、反馈用途和可退出方式应清楚，测试应包含模糊请求和错误输出。

依据：[Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai)；具体业务授权继续沿项目既有规则。


## 层级内容、展开与持续编辑

把集合、表格和树按任务区分：图像浏览可用网格，属性比较保留行列，父子对象用可展开层级。树节点的顺序与同层排序分别处理，筛选后仍能理解命中对象的归属。返回时恢复有价值的展开状态；以路径、搜索或分栏帮助定位，不强迫业务树只有两层。[Collections](https://developer.apple.com/design/human-interface-guidelines/collections) · [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views)

折叠入口说明会展开什么，并靠近相关对象；不能只因为一段信息叫“高级”就默认它不重要。可比较的信息若被收起，核对任务是否因此增加往返。Apple对某种disclosure button“一视图一个”的建议不代表列表只能展开一项；手风琴是否允许多项展开，取决于比较需求和空间。[Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls)

已知选项与允许自由输入是不同承诺；组合输入的自定义值不自动进入共享字典，新增选项沿实际权限处理。搜索条件胶囊应可辨认、编辑、移除并支持合适的键盘操作，不把中文输入中的标点或回车机械当成条件已确认。[Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes) · [Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields)

短字段与长文本选合适的编辑容器；有复用价值的款号、错误信息和路径应便于复制。软键盘类型帮助输入，不代替校验；键盘打开后保留输入位置、错误和下一步，按目标系统处理覆盖与滚动，不能把某平台“键盘独立窗口”推广到手机网页。[Text views](https://developer.apple.com/design/human-interface-guidelines/text-views) · [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards)

文档编辑的自动保存、导出副本与正式业务提交分别表达。自动保存只在真实支持时使用，并核文件位置、命名、格式与失败状态；保存草稿不能暗中转成已发布记录。跨应用使用文档时，预览、选择位置、导入/导出是否由系统承担按平台决定。[File management](https://developer.apple.com/design/human-interface-guidelines/file-management)


## 智能建议、预测与纠错

先区分预测是核心还是辅助、主动出现还是用户请求、涉及什么数据，再设计呈现与失败路线。给能核对的依据和适当不确定性说明；未经校准的置信值不包装成准确率，不把推测的情绪当事实。识别、排序、推荐和生成式结果都需要适合其后果的改正与手动路径，纠错本身也能改回。

点击或停留不直接证明偏好；界面变化本身会影响行为信号，不能直接归因模型改善。主动建议按相关性与打扰成本取舍，反馈用途和数据管理说明清楚；Apple对隐式反馈的建议不构成默认采集授权。沿[用户控制](user-control.md)处理数据与权限，沿[验证](evaluation.md)核实际任务结果；普通无模型界面不必增加AI流程。[Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning)



## 值选择、动作菜单与导航位置

持续选择一个值的菜单应让人看到当前选择；执行动作的菜单让人预测动作对象和结果。Apple的pop-up/pull-down是具体控件语义，迁移到Web时先分清值、动作、导航再选实现，不能仅凭“下拉框”外观决定行为。高频主要动作保持直接入口；菜单长度按发现成本与任务取舍，不照抄“至少三项”的跨平台门槛。[Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons) · [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)


## 记录、读数与内容位置

一次完成、可重复事件、多步清单和持续会话有不同的数据含义。重复记录保留时间和次数；持续会话区分开始、暂停、继续与结束，结束摘要对应真实记录。传感器不可用时区分缺失、估算和仍有效的值；不能把某种极短健身会话可丢弃的建议推广成自动删除生产记录。这是从[CareKit](https://developer.apple.com/design/human-interface-guidelines/carekit)与[Workouts](https://developer.apple.com/design/human-interface-guidelines/workouts)提炼的任务方法，不包含医疗判断。

仪表说明值在什么范围内，容量、进度和评分各有含义；显示精度不能悄悄改写原始数据。只读评分与可编辑评分分清，圆环闭合也不能掩盖超量或未知。[Gauges](https://developer.apple.com/design/human-interface-guidelines/gauges) · [Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators)

同层相关内容可用标签页，有序内容可用页码或位置点，深层对象沿父子链用路径或列式浏览；需要比较多个属性时仍考虑表格。截断路径保留查回祖先的方式。分页数量和标签数量取决于内容与宿主，不照搬固定上限。[Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views) · [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) · [Column views](https://developer.apple.com/design/human-interface-guidelines/column-views) · [Path controls](https://developer.apple.com/design/human-interface-guidelines/path-controls)

选色与图片替换应明确作用对象和属性；删除图片后的占位不能伪装成另一件商品的真实图片。剪切包含剪贴板动作，与直接删除分开。数字凭证需要专门输入时再按平台处理，不把电视PIN界面推广成数量或款号字段的默认形式。[Color wells](https://developer.apple.com/design/human-interface-guidelines/color-wells) · [Image wells](https://developer.apple.com/design/human-interface-guidelines/image-wells) · [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus) · [Digit entry views](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views)
