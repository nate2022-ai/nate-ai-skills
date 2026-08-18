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

本仓库版本是面向中文 AI 办公工作流的独立重构，增加了事实/决策分离、条件式双向钢人、决策账本、三道提问准入、95% 理解闸、停车闸、验收证据和研究规划模板。

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
