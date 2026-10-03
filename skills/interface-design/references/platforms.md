# 跨平台与尺寸适配

适用：Web、移动Web、小程序、iOS/iPadOS、Android和桌面应用的设计与迁移；另含腕上、电视、空间/AR与游戏的按需方法。范围覆盖不等于所有平台已实测；具体API、系统版本和宿主能力在实现时查当前官方资料。

## 先判断条件，再决定形态

把设备条件拆开看：可用窗口宽高、缩放与文字设置、输入方式、可见区域/安全区、网络与任务中断、平台导航语义。不要仅按设备名决定布局：桌面可以窄窗口，平板可以接键盘，手机也可能外接显示器。

保持任务、对象含义、状态和品牌语气；按空间重组导航、列表与详情、工具与内容。切换后保留合理的选中项、查询、输入和阅读位置。布局断点来自内容关系开始失效的位置；已有平台自适应框架适用时复用，不额外模拟一套窗口分类。

从一个平台借鉴时明确：系统已负责哪些行为，作者还要实现什么。例如原生系统提供的焦点导航、材质对比适配、文字放大与返回行为，不会因外观相似自动出现在Web自制组件中。

## 按目标平台落实

| 平台 | 主要设计判断 | 实现时核实 |
|---|---|---|
| Web / Mobile Web | 内容重排、浏览器历史和链接、键盘焦点、触控与悬停并存、文字放大 | 当前浏览器能力、语义HTML、读屏、软键盘与视口变化；不能把悬停当唯一操作 |
| iOS / iPadOS | 系统导航、列表到详情、多窗格、手势与可替代操作、系统文字样式 | 当前HIG、系统组件实际行为、Dynamic Type、安全区、键盘与辅助技术 |
| Android | 保留产品语义，按Android导航/返回方式及窗口组织内容 | 目标版本Material/Compose或既有技术栈、窗口变化、系统返回、输入和无障碍 |
| Desktop | 并列比较、多窗口、菜单与快捷键、密集操作、精确指针和键盘 | 目标桌面系统惯例、可调整窗口、焦点与菜单语义，不默认等同macOS |
| MiniApp | 宿主导航与页面生命周期、常见单手操作、网络中断和授权状态 | 实际小程序平台、版本、原生组件能力、安全区、键盘、返回与恢复；未核宿主文档不声称全部支持 |

使用原生控件通常能得到平台行为，但仍需核项目配置与实际结果。自定义控件有收益时可以使用，同时承担语义、输入、反馈和无障碍实现。跨平台共享视觉角色，不要求各平台像素相同。

Android官方自适应资料以应用窗口、姿态和输入为条件，支持窄窗口单区域、宽窗口并列区域等组织；迁移时保留状态连续。这里采用方法，不绑定某个Compose API版本。[官方依据](https://developer.android.com/develop/ui/compose/layouts/adaptive/get-started-with-adaptive-apps)

## 空间变化时保留什么

先列出当前任务必须共同看到的关系，再决定顺序、栏数、同时显示区域和展开方式。内容可以从并列变为顺序，也可以从双栏变为列表到详情；不要把重要操作直接消失作为响应式完成。

窄空间下比较任务仍可能需要表格：让确有二维意义的内容区域滚动，提供身份与滚动线索，旁边的搜索、说明和操作正常重排。WCAG Reflow对有二维意义的区域有例外；例外不自动覆盖整页或单元格长文本。[W3C解释](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)

大字号与本地化可能比缩窄更早破坏布局。检查长中文、长英文、数字单位、双向文字（实际涉及时）、多行标签和控件文本。不要用图片替文字绕过缩放。

## 输入与平台数值

触控区域、可见图标和视觉尺寸可以不同。Apple按钮的44×44 pt建议有原生平台上下文；不能抄成所有Web控件44px的硬门槛。Web目标尺寸标准具有自己的单位、条件与例外；按选定标准检查，同时考虑实际误触。[Apple Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) · [WCAG 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

鼠标悬停可提高发现性，但触控和键盘仍应能触发核心操作。使用系统或框架提供的焦点/键盘能力时先核职责；不能断章取义用Apple某平台的系统代办说明，免除Web作者的键盘实现责任。

## 验证与未覆盖范围

按实际目标验证：窗口改变、方向改变、软键盘出现、文字放大、相关输入以及返回/恢复。模拟器可以支持布局和部分交互证据，真机触摸、性能或硬件反馈仍分别说明。Web实现或截图可用于跨平台方案沟通，不能作为原生应用运行验收。

现有首批早期网页试点样本从1440×900和390×844内容区域起步，这是试点观察条件，不是跨项目强制尺寸。新项目沿自己的目标窗口与断点条件选择，必要时补中间状态。

进一步依据与本轮阅读状态见[sources](sources.md)。


## 多窗口、切换与导航收缩

多窗口用于并行处理对象、保留现场或对照，不只是宽版布局。区分主窗口、辅助任务和当前接收输入的窗口；快捷键与模态只影响它们应影响的对象。是否默认新开窗口取决于任务，避免每次查看都产生新窗口。[Windows](https://developer.apple.com/design/human-interface-guidelines/windows)

切走和回来时恢复对象、阅读位置、编辑与处理状态。需要持续参与的过程可以暂停；上传能否在后台继续以系统和服务能力为准。返回时重新核权限、数据版本及结果，不把旧画面当成已完成或仍有效的事实。[Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)

多栏表达父子关系时保留选中链，缩窗后变成可追溯导航；隐藏栏同时设计恢复入口，中间宽度也要检查。顶层目的地不应仅因暂时无数据而跳动；权限隔离与产品不提供的功能另外处理。工具按作用对象分组，收缩时安排溢出次序，并保留完成/返回及明确名称。侧栏层数、标签数量、工具组数是具体平台建议，不是企业界面的通用上限。[Split views](https://developer.apple.com/design/human-interface-guidelines/split-views) · [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) · [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) · [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)

折叠、姿态和系统保留区域改变时，尽量只调整必要部分，保持对象与操作语义。设备专属工具栏、API和行为只在确认目标平台版本后采用；不把某款设备的适配方式写成所有Web页面要求。[平台专项入口](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)


## 空间、腕上、电视与游戏

**空间与AR。** 先判断空间呈现是否帮助任务，再选择窗口、混合或更强沉浸；进入强沉浸有明确操作，退出、暂停与恢复保留控制权。关键内容位于舒适视野，不把初始位置适配解释成随头部固定。深度用于层级时核文字清晰与反复聚焦负担，真实商品比例与控件可选性分别处理。常用头显操作考虑手臂放松的间接输入，不能把空间角度直接换算成Web像素。[visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos) · [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences) · [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)

手持AR另核设备、光照、表面与活动空间。能力不足时给可用替代；放置反馈区分估计表面和已稳定关系，用于尺寸判断时保留物理比例，区别移动与缩放。按移动姿势、目标大小和稳定性选直接操作或屏幕控件。中断后说明恢复过程，必要时暂藏位置不可靠的物体，失败时给取消或重来；用用户能做的动作描述恢复建议。空间舒适度、跟踪与硬件输入要由目标设备验证。[Augmented reality](https://developer.apple.com/design/human-interface-guidelines/augmented-reality)

**腕上与电视。** 抬腕短时查看围绕关键内容和迅速处理，复杂编辑移到合适承载处；应用、表盘入口和通知各有作用。电视按真实观看距离检查阅读与遥控焦点，多人共享时核当前身份。腕上不等同所有小屏，电视也不等同近距离桌面宽屏，二者不能套同一简化模板。[watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos) · [tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)

**游戏。** 可玩教学和合理默认值可帮助开始；迁移到业务软件时改成低风险真实任务，不省略高后果操作的必要说明。触控、键鼠、遥控、手柄分别安排映射和可替代输入，核字号、声音、运动强度的可调整性。跨设备进度恢复取决于真实同步能力。页面中的默认/最小按钮尺寸口径需结合控件专页与目标平台核实，不抽成跨平台硬阈值。[Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)

## 采集、宿主与启动恢复

支持Camera Control的拍摄界面保留取景面积，协调系统浮层与应用控件；连续参数显示单位与有意义的停靠值，离散选项用对应选择方式。硬件滑动上的排序建议不通用于网页工具栏。锁屏启动只进入相应采集范围。[Camera Control](https://developer.apple.com/design/human-interface-guidelines/camera-control)

照片编辑明确预览、应用、保存和丢弃的后果。有未保存修改且退出会丢失时适当保护，可可靠恢复或未修改时不机械加确认。宿主已有工具栏时协调职责；Photos保存原件的机制不证明自建编辑器天然无损。[Photo editing](https://developer.apple.com/design/human-interface-guidelines/photo-editing)

允许连续访问多页的内嵌网页，提供真实后退/前进；单页预览按任务提供关闭或返回外层的路径。选系统浏览方式或自建容器时看任务与维护责任，不假定容器已提供完整导航能力。[Web views](https://developer.apple.com/design/human-interface-guidelines/web-views)

启动过渡与首个可用界面保持主题和方向连续，教学与欢迎在各自流程处理；不延长启动展示，也不制造已就绪假象。恢复时核真实数据、权限和未保存内容。全屏用于有专注收益的任务，保留核心控制和熟悉的工具恢复方式；进入、退出及切换应用保持现场，暂停取决于错过内容的后果。iOS启动画面限制和游戏防误退出机制不成为所有网页的通用要求。[Launching](https://developer.apple.com/design/human-interface-guidelines/launching) · [Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)



## 专用宿主与领域入口

以下仅在项目实际采用时查阅；研究过界面方法不代表已接入其API。模板、数值、系统标识与功能支持范围按目标版本核实，不进入通用Token默认值。

| 场景 | 可复用判断与专有边界 | 官方入口 |
|---|---|---|
| 桌面系统菜单 | 菜单按应用/文件/编辑/显示等职责组织，稳定命令与上下文动作分别处理；菜单栏图标不能承担唯一入口 | [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar)、[Dock menus](https://developer.apple.com/design/human-interface-guidelines/dock-menus) |
| 系统快捷与结果片段 | 高价值动作可独立完成，短结果说明实际状态，长任务进入对应对象；App Shortcuts与App Intents的支持范围分别核 | [App shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts)、[Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets)、[Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions) |
| 腕上常显、表盘入口 | 常显保留熟悉位置并收敛变化；时间线与读数新鲜度明确；共享表盘配置不等于任意创建系统表盘 | [Always On](https://developer.apple.com/design/human-interface-guidelines/always-on)、[Complications](https://developer.apple.com/design/human-interface-guidelines/complications)、[Watch faces](https://developer.apple.com/design/human-interface-guidelines/watch-faces) |
| 电视内容入口 | 图文组成聚焦单元并预留放大空间，选择后直达相关内容；不迁移成商品款号只能悬停显示 | [Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups)、[Top Shelf](https://developer.apple.com/design/human-interface-guidelines/top-shelf) |
| 系统控制区域 | 空间工具区保持与窗口关系，避免重复系统已提供的壳；系统状态栏不等于网页必须仿制时间电量 | [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments)、[Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars) |
| 车载 | 任务沿实际支持的系统模板组织，配置前置到停车时；驾驶中不依赖拿起手机完成核心流程 | [CarPlay](https://developer.apple.com/design/human-interface-guidelines/carplay) |
| 家居 | 设备名称、家庭与房间等共享设置保持一致，修改共享来源体现明确用户意图；不把可选云账号后置推广成所有软件免账号 | [HomeKit](https://developer.apple.com/design/human-interface-guidelines/homekit) |
| 健康与研究 | 数据请求对应真实任务；记录、参与说明、理解与同意各有流程；界面指南不证明临床有效或替代伦理/法律判断 | [HealthKit](https://developer.apple.com/design/human-interface-guidelines/healthkit)、[ResearchKit](https://developer.apple.com/design/human-interface-guidelines/researchkit)、[CareKit](https://developer.apple.com/design/human-interface-guidelines/carekit) |
| 游戏社交与运动输入 | 邀请直达玩法，排行榜区分周期与终身口径；体感数据有任务收益才使用，不迁移成员工绩效模板 | [Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center)、[Gyroscope and accelerometer](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer) |

Apple Activity rings有特定健康含义和标识规则；自己的KPI或进度图使用不混淆的表达，不把系统三环当通用图表皮肤。[Activity rings](https://developer.apple.com/design/human-interface-guidelines/activity-rings)


## 外部服务与内容迁移

链接、扫码、轻量入口或消息扩展应接到指定对象和步骤，保留已完成的输入；必要账号和权限前置仍可存在，不因换入口无故重填。迁移到桌面重新安排窗口、菜单和输入，不能只放大移动界面。[App Clips](https://developer.apple.com/design/human-interface-guidelines/app-clips) · [iMessage apps and stickers](https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers) · [Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst)

| 实际采用的服务 | 设计时查什么 | 官方入口 |
|---|---|---|
| 购买、订阅与票证 | 总额/周期/已有权益、取消恢复、订单/支付/履约分别表达；品牌按钮、服务资格与接口不能由一般方法替代 | [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay)、[In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase)、[Wallet](https://developer.apple.com/design/human-interface-guidelines/wallet) |
| 身份与账号 | 当前任务所需信息、身份连续、拒绝后的路线；专有认证、证件资格和标识另核 | [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)、[ID Verifier](https://developer.apple.com/design/human-interface-guidelines/id-verifier) |
| 近距感知、标签和声音识别 | 作用对象、采集中与已取得结果分明；识别许可不推导长期保存许可 | [Nearby interactions](https://developer.apple.com/design/human-interface-guidelines/nearby-interactions)、[NFC](https://developer.apple.com/design/human-interface-guidelines/nfc)、[ShazamKit](https://developer.apple.com/design/human-interface-guidelines/shazamkit) |
| 媒体输出与共同观看 | 输出用户选择的媒体，区分串流与镜像，避免无意传出其他界面；共同行为与个人控制分开 | [AirPlay](https://developer.apple.com/design/human-interface-guidelines/airplay)、[SharePlay](https://developer.apple.com/design/human-interface-guidelines/shareplay) |
| 动态素材、直播与回放 | 类型与可用状态明确；不支持时说明退化，分享前看清将发什么 | [Live Photos](https://developer.apple.com/design/human-interface-guidelines/live-photos)、[Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps) |
| 地图与打印输出 | 地图聚合随观察尺度，选中对象与详情保持关系；打印选项与预览反映真实设备能力 | [Maps](https://developer.apple.com/design/human-interface-guidelines/maps)、[Printing](https://developer.apple.com/design/human-interface-guidelines/printing) |

这里提供方法与来源入口，具体品牌、协议、格式、地区支持和当前发布条件在实施相应功能时核实。
