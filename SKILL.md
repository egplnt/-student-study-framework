---
name: student-study-framework
display_name: 高中生学习工程框架
display_name_en: High-School Study Engineering Framework
description: Reusable high-school study-engineering framework — scan gaps → bridge, 5-step daily loop, parameterized red-line checklist.
description_zh: 一套可复用的高中生学习工程方法论框架（适用于 WorkBuddy 智能体）。涵盖扫盲点→搭桥、每日五步闭环、参数化红线清单；含思路起源、前置依赖与效果边界。已完全脱敏。
description_en: A reusable study-engineering methodology framework for high-school students (for WorkBuddy agents). Covers scan-gaps→bridge, a 5-step daily loop, and a parameterized red-line checklist. Fully anonymized.
examples_zh:
- "帮我给高一数学做一次扫盲点，列出知识跳跃点并设计桥接计划"
- "生成这周的周任务单和每日五步闭环清单"
- "按红线清单校验我今天的学习计划"
examples_en:
- "Run a gap scan for first-year high-school math, list the knowledge jumps and design bridge plans"
- "Generate this week's task sheet and the daily 5-step loop checklist"
- "Check my study plan against the red-line checklist"
category: education
version: 1.1.0
author: egplnt
agent_created: true
---

# 高中生学习工程框架（核心框架）

> 本 skill 已完全脱敏，使用中性示例表述，不依赖任何内部代称或代号。
> 本框架不承诺提分。术语定义、证据分级与失效条件见 `README.md`；效果边界见下节。

## 何时使用
- 构建或维护高中生的学习计划、知识搭桥、周任务单、组题链路、红线校验时触发。
- 涉及「扫盲点→搭桥」方法论、每日闭环时触发。

## 前置依赖与效果边界（必读）
本框架交付的是**方法论骨架**，不含任何数据资产与人力。效果强依赖以下外部条件，**非开箱即用**：

**硬前置条件**
1. **本地学习资料库**：需要一套分学科、可检索的本地资料（教辅 / 试卷 / 讲义），桥接计划才有素材。库为空、或资料是无文字层的扫描件时，须先做 OCR 或建立路径索引。
2. **每日人力统筹**：五步闭环的第 ②③④⑤ 步（手写执行、三查、送批、对答案）须由家长 / 统筹人每日执行。无此角色，闭环断在中途。

**效果边界**
- 本框架能从零建立「计划—执行—校验」的流程纪律，但**不会自动产生提分效果**。
- 效果 ≈ 方法论 × 资料资产 × 每日人力投入 × 环境适配；本 skill 只提供第一项的一部分。
- **学科适配**：框架在理科（数学 / 物理 / 化学）验证较充分；文科、低龄、大学阶段需自行调整桥接逻辑。
- 红线清单条目多为具体案例沉淀，使用时须按自身学情裁剪，**不可照搬**。

## 一、核心定位（参数化，可套用不同学生）
以一个高中生为示例，框架对以下参数开放：
- 学段 / 科目 / 高考年份 / 目标分段
- 主线教辅
换一名学生时，仅替换上述参数即可复用，不必重写流程。

## 二、核心方法论：扫盲点 → 搭桥（scan gaps → bridge plans）
1. **scan gaps**：定位知识跳跃点与概念卡点。
2. **bridge plans**：为卡点设计搭桥计划（B/D 桥接）；概念卡点设独立「概念攻坚补充」附件隔离，攻破后再恢复后续测试。
3. **gating tests**：桥接完成后设闸门测试，通过才进入下一阶段。

## 三、执行节奏：每日五步闭环
① 生成打印清单 → ② 手写执行 → ③ 90 秒三查勾选（查完成度 / 查规范 / 查疑点）→ ④ 难篇 / 续写拍照送批 → ⑤ 对答案报结果。
配合周任务单与交接单：当日未闭环项转入次日首条；新发现的卡点记入桥梁资产或概念攻坚附件。
模板见 `references/daily_loop.md`。

## 四、红线清单（逐条可勾选）
**进度 / 内容红线**
- [ ] 超前内容不提前拖入低周次（如高二下内容不进入高一进度）
- [ ] 英语读后续写以校情过关线为基线（如 75 词，非高考 150 词），严禁加量欠写
- [ ] 每篇三查必做、难篇必送批
- [ ] 概念卡点设独立「概念攻坚补充」附件隔离，攻破后再恢复闸门测试

**工具 / 数据红线**
- [ ] 资料盘零丢失、永不自动删除、每批 ≤10、先清单再确认、同盘 move 可逆
- [ ] PDF 处理前先跑文字层预检，禁止默认「PDF 有文字」
- [ ] 对外交付文件一律脱敏，禁止出现任何内部代称

完整勾选表见 `references/redline_checklist.md`。

## 五、输出格式约定
- 单栏 HTML、顶部 TOC、零依赖可离线、可打印。
- 相对路径链接、well-formed 校验、旧版零残留。
- 交付前四闸门预检（控制层 / 内容源 / 格式核对 / 库缺口）：若已安装 `study-deliverable-precheck` 则按其流程执行；未安装时按本节四项逐条自检。

## 六、关联
- 通用搭桥方法论由 `study-plan-bridge` 覆盖；本 skill 只收专属部分（参数 + 红线 + 五步闭环），通用部分引用即可，不重抄。**该 skill 未上架官方市场，未安装时直接按本文件第二节执行即可**，不影响本 skill 独立可用。
- 可选扩展模板见 `references/`：`daily_loop.md`（五步闭环 + 周任务单）、`redline_checklist.md`（红线勾选表）。
