# 交互、反馈与动效

适用：按钮、弹层、选择、拖动、切换、加载等交互，以及动效和多种输入方式。整合Apple设计目的、Emil交互经验与现有方法；具体数值为项目选择，除明确引用平台要求外不写成通用限制。

## 从意图到状态

先说明触发、作用对象、正在进行的过程、完成/失败/取消，再选动画形式。按钮应有及时、可辨认的反馈，但不必全部缩放；已提交、正在提交、仅按下是不同状态。连续点击、快速切换和异步返回不能把界面带回过期状态。

默认组件的交互语义通常比自造可点击容器更可靠。链接用于导航，按钮用于动作；开关、单选、复选与菜单表示不同决策。原生平台按各自组件约定落实，避免为外观统一牺牲熟悉的行为。

禁用状态说明真正的限制；当用户需要知道如何解除时给出原因。空白点击、按键、返回和外部点击的效果按容器语义决定，避免全页面无差别绑定快捷键。

## 弹层、非模态面板与焦点

先判断是否必须中断当前任务。模态弹层用于需要当前决策或独立完成的流程；查看补充资料或并行操作可用非模态面板。不要因实现方便把所有详情变成模态。

Web模态要有明确名称、合适初始焦点、在打开期间合理约束焦点和背景交互、关闭后的返回位置；按适用语义支持关闭方式。仅设置role或aria-modal并不会自动实现全部行为。[MDN dialog](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/dialog_role)

原生系统组件优先核实际提供的行为，不在外层重复模拟焦点或返回。退出前有未保存内容时按真实保存能力处理；非模态面板不照搬模态的全部限制。

## 动效选择

| 用户需要理解什么 | 可用表达 | 重点检查 |
|---|---|---|
| 操作已被接收 | 颜色、按压或状态变化 | 反馈及时，不等远端完成才响应 |
| 内容从哪里来、到哪里去 | 与触发位置相关的展开、位移或共享元素关系 | 因果清楚，返回连续 |
| 数据或状态发生变化 | 局部突出或稳定替换 | 不干扰读数，不伪造中间业务值 |
| 可拖动对象被抓住或吸附 | 跟手位置、约束与必要动量 | 中断、反向和合法目标清楚 |
| 品牌或低频重要时刻 | 有节奏的进入或重点表现 | 与内容相关，可跳过或不阻塞下一步 |

按距离、内容规模、操作频率和设备调整节奏。高频任务减少等待和视觉漂移；低频表达也不自动需要复杂动画。先复用项目已有动效变量；没有时可选择短、中、长几个有用途的参数，实测后调整，不能把某位作者的毫秒上限写成Apple统一规则。

缓动表达加速/减速与响应感；弹簧适用于需要连续追随、中断或动量的场景，不是所有入场的必选项。动画应能处理快速连续操作，不能阻塞新的意图或退出。缩放原点、进退方向和结束状态与空间关系一致。

## 手势与替代操作

拖动应保留抓取位置，明确可放置区域、取消和失败结果；滚动与拖动竞争时先处理方向和触发条件。速度阈值、距离和阻尼从实际组件与平台行为出发，不能把示例物理公式直接当标准。

核心任务提供适用的替代路径，例如移动上下按钮、菜单或点击目标；Web的拖拽替代还要看单指针要求，只有键盘替代不一定满足该项。[WCAG Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)

声音与触觉按平台能力、任务和用户设置使用，与真实事件同步并提供其他可理解反馈。没有硬件或权限证据时不宣称已实现。

## 可访问性与性能一起设计

减少动态效果时，削弱大范围位移、视差与反复运动，同时保留理解所需的状态变化；不机械删除所有反馈。透明度、颜色和阴影也应检查实际可读性。

Web动效常可优先使用较易合成的属性，但是否顺畅要看实际渲染、范围和设备。模糊、大阴影和大面积动画需要对应观察；不要通过一律禁止某属性代替判断。动画参数静态正确不证明运行流畅。

检查慢速状态转换，也检查快速连续输入、取消、焦点返回与减少动态效果。动效应与实际数据和用户操作一致，不能借漂亮过渡掩盖等待或错误。


## 临时容器与提交语义

| 要完成的事 | 可考虑的形式 | 退出时核查 |
|---|---|---|
| 当前必须处理的问题 | 警示框 | 原因、可行选择及误操作后果清楚 |
| 短暂的独立步骤 | Sheet或模态任务 | 完成、取消、返回各自含义明确；长任务再评估页面或窗口 |
| 查看或微调关联对象 | Popover | 锚点与参照清楚，空间不足可换容器 |
| 反复操作并观察主界面 | 非模态面板或多栏 | 主界面仍能操作；不套模态焦点锁定 |
| 快速操作当前对象 | 上下文菜单 | 核心动作仍有可发现入口 |

外部点击关闭、保存草稿、即时修改、正式提交是不同语义。Popover关闭不应无声丢输入，也不能据“自动保存”推导自动发送、批准或更改业务记录。临时界面需要嵌套时明确层级与返回目标，不用“永不嵌套”代替流程判断。

依据：[Modality](https://developer.apple.com/design/human-interface-guidelines/modality)、[Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)、[Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)、[Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers)、[Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus)。

## 焦点、拖放与撤销

焦点表示当前输入位置，选中表示对象或选择状态，激活表示执行。移动焦点不一定立即激活；刷新不应无故夺走焦点，原项消失时安排可理解的接续目标。快捷键沿平台熟悉语义，不截获输入法或文本编辑所需命令；专用动作再按频率增加快捷键。[Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) · [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards)

拖放先定义移动、复制或建立关联，再显示可接收位置与范围。多项拖入说明数量、部分接受和未完成项；传输慢时落点可显示明确占位。接收失败不能像已完成一样留下内容，已有对象不能因前端动画先消失而实际丢失。提供当前实现确实具备的恢复路径。[Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)

撤销名称说明将撤销的动作与对象，执行后让人找到结果。连续小改动可按一次意图合并，独立业务提交不能随便合成一个撤销组。跨人编辑、外部发送和跨会话恢复须核真实机制，不承诺无限撤销。[Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)

等待时让无依赖操作继续；能测量进度时才显示确定值。进度停滞可以说明阶段或恢复办法，不能为了动画不断前进而编造百分比。取消、暂停、后台继续各自需要真实能力支持。[Loading](https://developer.apple.com/design/human-interface-guidelines/loading) · [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)


## 滚动与对象相关操作

让溢出内容能被发现，保持熟悉的滚动和键盘行为。同方向嵌套滚动容易争抢输入；确需嵌套时明确区域边界和滚动接续。定位搜索结果、输入光标或操作对象时只滚动必要距离，不把每次刷新都变成回到顶部。平台的滚动边缘效果用于分隔浮动控件和内容，不是装饰性的全页渐变。[Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views)

用户主动动作后需要选后续处理方式，与系统突然出现的问题是不同情境；选择菜单、确认面板或警示框时保留这种差异。选项数量、破坏性按钮位置、回车默认行为按平台和后果核查，不能把危险动作设成最容易误触的默认项，也不把普通操作都加一道确认。[Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets) · [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)

对象检查器随当前选中项更新，固定详情窗口则保持原对象；标签与状态让用户知道正在改谁。macOS的NSPanel窗口行为不直接适用于Web侧面板，内容可编辑时仍需处理输入与未保存状态。[Panels](https://developer.apple.com/design/human-interface-guidelines/panels)

可见按钮大小、命中区域、控件间距与默认角色是不同参数。不要从某一张平台尺寸表推导通用最低像素；自定义按钮要有能感知的响应，并让等待、成功和失败各自对应真实过程。[Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)


## 媒体会话与精细输入

播放、短提示、录音和通话需要不同的声音共存与后台策略。尊重系统音量和输出设备；耳机断开、来电结束、返回页面分别决定暂停或恢复，不能统一自动开麦或播放。外部播放键只作用于当前会话。系统音频分类属于平台实现，不照抄到普通Web页面。[Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio)

视频优先采用适用的成熟播放器，保留播放、暂停、字幕和目标输入方式的熟悉操作。完整显示与裁切填满是不同选择，不能以拉伸变形适配；证据或商品画面还要核裁切会否丢掉关键信息。切内嵌、全屏、画中画时保持进度并协调声音，退出回到可继续的位置。字幕等替代内容见[多感官与辅助输入](evaluation.md#多感官辅助输入与本地化)。[Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video)

触觉与真实事件同步，含义稳定；系统成功反馈不用于失败。高频操作按实际负担调节反馈密度，关闭触觉仍能理解状态；录音、拍摄或传感器采集时还核振动影响。持续触觉可适合游戏，不自动用于普通业务任务。[Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)

手写与绘制让反馈贴近笔尖，考虑左右手遮挡。书写中不移动输入目标，必要重排等停笔后进行；悬停用于预览，不触发破坏动作。捏合、双击沿设备能力和用户设置，误触可能性高时宜作用于可恢复操作。原图标注还要核主题变化是否改变标记含义。[Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble)



## 硬件与语音输入的任务语义

实际采用手柄、遥控、旋钮或动作按钮时，提示匹配当前设备与动作，区分触碰、聚焦和有意执行。旋转方向和可见结果连贯，系统保留的返回、主界面与暂停动作按宿主处理。游戏中的复合动作和隐藏摇杆不直接成为业务录入规则。[Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) · [Remotes](https://developer.apple.com/design/human-interface-guidelines/remotes) · [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown) · [Action button](https://developer.apple.com/design/human-interface-guidelines/action-button)

语音动作名称说明对象和结果，回复可独立理解成功、等待或失败；必要追问指出缺什么，选项太长先缩小范围。系统识别实体、执行意图与索引内容需要实际接入，文案本身不证明这些能力存在。[Siri](https://developer.apple.com/design/human-interface-guidelines/siri)

visionOS注视反馈表达可交互性；系统出现高亮不代表应用可获得注视事件或据此触发业务动作。自定义效果保留稳定部分，避免出现新内容反而抢走当前目标；数值和实现职责查目标平台专页。[Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)
