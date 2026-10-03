# 第三方来源与许可声明

## Matt Pocock `grilling` Skill

本仓库的 `grill-requirements` 在方法上受到 Matt Pocock 的 `grilling` Skill 启发，尤其包括：

- 默认一次只问一个问题；
- 沿决策树逐步解决依赖关系；
- 每个问题提供推荐答案；
- 能从环境中查到的事实先查，不反问用户；
- 达成共同理解前不实施。

上游来源：

- 项目：<https://github.com/mattpocock/skills>
- 本次核对提交：`9c9f36ccd3995266cd675468af71639c8dde1ec5`
- 文件：<https://github.com/mattpocock/skills/blob/9c9f36ccd3995266cd675468af71639c8dde1ec5/skills/productivity/grilling/SKILL.md>
- 许可：MIT License

本仓库版本是面向中文 AI 办公工作流的独立重构，采用事实与决策分离、条件式目标校准、必要提问过滤、安全最小试验、按主题分组讨论、停车闸和可观察的验收条件。主入口按需选用规划、任务书、长任务接续及协作材料；当前行为以本仓库的 Skill 正文为准。

上游许可声明如下：

```text
MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## KKKKhazix `leader` Skill

`grill-requirements` 的执行任务书模式在方法上受到 KKKKhazix `leader` Skill 启发，尤其包括：

- 使用写入白名单约束执行地界；
- 先用“任务 0”核验命令、环境和基线；
- 冻结验收标准并防止跳过测试、弱化断言等作弊达标；
- 对静默失败做反向验证；
- 设置连续失败、结果退化、越权请求和不可逆动作的止损与停车闸；
- 要求结构化回执，并将执行者自报与独立终验分开。

上游来源：

- 项目：<https://github.com/KKKKhazix/khazix-skills>
- 本次核对提交：`7a5c4934be4106ac740ffdb95280bb81b3f4b83c`
- 文件：<https://github.com/KKKKhazix/khazix-skills/blob/7a5c4934be4106ac740ffdb95280bb81b3f4b83c/leader/SKILL.md>
- 许可：MIT License

本仓库没有把上游 `leader` 作为运行依赖，也不是逐句翻译或原样复制。相关方法已按本仓库的双模式路由、授权边界、Codex 正式任务和 Goal 分流重新设计，并内建于 `grill-requirements`。

上游许可声明如下：

```text
MIT License

Copyright (c) 2026 数字生命卡兹克

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 界面设计 `interface-design`

本Skill将设计知识与已有方法按任务重新组织为中文工作流程。Apple Human Interface Guidelines是主要知识来源，frontend-design、Impeccable、Emil design-eng、UI/UX Pro Max及Vercel web-design-guidelines提供方法参考；具体固定版本、采用范围、历史许可核查与限制见[来源与转化](skills/interface-design/references/sources.md)。这些来源不是必须安装的运行依赖。

设计奖与优秀案例来自Apple Design Awards、Awwwards、CSS Design Awards、UX Design Awards及Red Dot等官方来源；身份核实与适用边界见[设计案例检索](skills/interface-design/references/design-case-research.md)。

本包提供自主整理、来源链接和脱敏研究，未整篇分发上游Skill正文或脚本，也未捆绑第三方完整网页、图片、视频、字体或UI Kits。仓库MIT许可适用于本仓库提供的内容，不改变所链接第三方材料、商标及资产的权利。来源引用、公开可读或获奖身份均不表示获得第三方素材的转载授权。

