# 通知、权限、账号与共享

用于设计跨出当前页面的提醒、数据访问、身份流程和多人协作。沿真实产品能力和既有授权落实，不把设计文案当作安全或合规证明；普通视觉调整无需读取本篇。

## 通知是否值得打断

按事件影响、时效及用户期待决定提醒方式。用户就在相关页面时可就地更新；离开当前页面后，信息值得及时了解或需要行动，且符合用户偏好时再通知。相同事件去重，未读数对应真实未读状态，点击后到相关对象；对象失效则给原因与可行去处。

通知预览避免泄漏不必要的私人或业务细节，操作明确且尽量可恢复。营销偏好与事务提醒分开，说明系统通知权限和应用内开关的关系。平台的紧急通知能力有使用条件，不作为普通提醒提高曝光的技巧。

例：导出完成可以在任务列表查到结果，只有用户确实需要离开页面等候时再考虑系统通知；审批临近截止是否打断由真实业务时效决定，不因写了“重要”就提升优先级。

依据：[Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications)、[Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)。例子是本地适配，未作业务验收。

## 权限请求与拒绝后的路线

在功能需要时说明将使用哪项数据、用途及可见结果。单项选择或有限授权足够时不扩大范围；拒绝后说明受影响能力与可行替代，并保留后续管理入口。额外引导屏是否需要，取决于系统提示能否说明清楚，不固定每次弹两层。

不要将Apple某种预权限屏的按钮要求推广为所有产品禁止退出，也不能认为“系统签名”就足以证明数据安全。用真实权限状态驱动界面；授权、访问控制、撤销和安全存储仍需实际实现与验证。正式发布涉及平台规则时查对应现行要求。

依据：[Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)。

## 账号的进入、退出与结束

先判断任务是否依赖身份。公开浏览可推迟登录；企业权限和私人数据可能必须先认证，解释原因即可。按钮只展示当前支持的认证方法，失败后提供可用的重试或替代通道，保留适合保留的输入。

退出登录、停用账号、删除账号、取消订阅是不同动作。界面说明实际影响、完成时间及尚未结束的处理；不要把“已提交删除请求”写成“全部数据已删除”。数据保留和账单规则来自真实系统及适用要求，不能由设计者自行补造。

依据：[Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)。

## 分享副本与多人协作

先区分发送一个副本，还是让别人访问同一个持续更新的对象。共享前说明谁可访问、能否编辑、能否再邀请；共享后有可见状态及管理入口。成员退出、权限变化、链接失效、并发更改与同步延迟分别表达，避免“已分享”掩盖无法访问。

例如共享生产计划链接不等于复制一份导出表；原对象更新是否会传到接收方，应与系统行为一致。系统分享面板可以减少学习成本，但CloudKit、Messages等整合只属对应平台实现选项，不是跨平台协作的前提。

依据：[Collaboration and sharing](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing)。

进一步来源与知识覆盖见[sources](sources.md)。


## 系统外部入口与持续状态

桌面/锁屏组件先明确一个主要用途，空间增加时补有用上下文；简单操作可原地完成，复杂编辑打开对应对象。更新受系统限制时不把旧值称为实时，必要时显示更新时间。系统可能重设颜色，因此状态同时有文字或形状线索。这些方法针对系统托管组件，不将任意网页卡片等同Widget。[Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets)

持续活动适合有开始、过程与结束的任务：保持任务身份、关键进度和必要操作，点击直达相关对象，任务结束及时结束“进行中”展示。不为同一更新重复多路提醒；公开屏幕注意私密性，用户能停止关注。无限期仪表盘和促销不自动套用该形态。[Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities)

系统快捷操作明确作用对象，区分当前状态、执行中与完成；图标独立出现也应能辨认。锁屏敏感内容和高影响操作按真实身份机制处理，不推成所有按钮都需解锁。打开完整应用接到对应任务；持续动画不能代替成功证据。[Controls](https://developer.apple.com/design/human-interface-guidelines/controls)

各入口尺寸、刷新预算和可用操作依赖宿主版本，沿[平台适配](platforms.md)核实；配图和尺寸表未逐项验证，不据本篇提供跨平台固定参数。



## 跨设备状态与分阶段完成

同步目标是让人继续工作，但“本地保存”“待同步”“云端已更新”不能混写。更新受网络、带宽或文件大小影响时显示真实状态；同步冲突让人能辨别版本并解决，删除影响其他设备时说明范围。平台提供同步机制不证明本项目已经支持离线或自动冲突合并。[iCloud](https://developer.apple.com/design/human-interface-guidelines/icloud)

把外部流程按真实业务阶段表达：设备读到信息、服务处理、处理成功及后续履约各有含义。例如Tap to Pay的系统勾号确认读卡完成，交易是否成功仍由后续处理结果决定。迁移到业务系统时，扫码成功不等于正式出库、本地保存不等于审核通过；这是本Skill的适配推论。等待和失败提供项目实际支持的恢复路径，结果不明时先核状态，不用重复提交制造“成功”。[Tap to Pay on iPhone](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone)


## 轻量扩展与系统共享设置

分享或轻量扩展承接当前对象，宿主和应用身份清楚；关闭入口不等于长任务完成，后台继续须真实支持。专门打印等动作若与通用动作结果不同，用名称说明差异。Apple的顺畅发送示例不授予AI外部发送权限，仍沿用户对具体对象和动作的授权。[Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views)

系统已管理的权限或共享设置，优先沿真实控制入口反映状态，不仿制一套含义不同的开关；调用授权接口不等于每次重复弹窗。改写共享数据要能理解对象和影响范围；相关平台细节见[专用宿主与领域入口](platforms.md#专用宿主与领域入口)。


共同会话中，影响全体的动作与个人调整分别表达，退出、重返和谁改了什么可理解。结束会话不自动等于保存或终止其他人的工作；媒体共看的冲突策略不能照搬到需要保留并发事实的生产记录。[SharePlay](https://developer.apple.com/design/human-interface-guidelines/shareplay)

登录、补充资料、评价或添加票证的请求贴近用途，区分必需与可选；已有身份和权益允许合理继续，不诱导重复注册或购买。评分请求避开用户正在完成的任务，拒绝后不反复打断，保留合适的主动入口。频率与品牌按钮等具体要求沿目标平台核实。[Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews) · [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)
