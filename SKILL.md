---
name: student-study-framework
description: This skill should be used when building or maintaining a high-school student's study plan, bridging knowledge gaps (scan gaps → bridge), daily execution loops, weekly task sheets, or a local-LLM question-generation + cloud-grading pipeline. It encodes a reusable "scan gaps → bridge" methodology, a 5-step daily loop, an Ollama local question-generation setup, and a parameterized red-line checklist, generalized across students via replaceable parameters (subject / exam year / target band / main textbooks).
description_zh: 一套可复用的高中生学习工程方法论框架（适用于 WorkBuddy 智能体）。涵盖扫盲点→搭桥、每日五步闭环、本机 Ollama 出题+云端判读、参数化红线清单；含思路起源、前置依赖与效果边界。已完全脱敏。
description_en: A reusable study-engineering methodology framework for high-school students (for WorkBuddy agents). Covers scan-gaps→bridge, a 5-step daily loop, local Ollama question-generation + cloud grading, and a parameterized red-line checklist. Fully anonymized.
version: 1.0.0
author: egplnt
agent_created: true
---

# 高中生学习工程框架（核心框架）

> 本 skill 已完全脱敏，使用中性示例表述，不依赖任何内部代称或代号。

## 何时使用
- 构建或维护高中生的学习计划、知识搭桥、周任务单、出题链路、红线校验时触发。
- 涉及「扫盲点→搭桥」方法论、每日闭环、本地模型出题 + 云端判读链路时触发。

## 前置依赖与效果边界（必读）
本框架交付的是**方法论骨架**，不含任何数据资产与人力。效果强依赖以下外部条件，**非开箱即用**：

**硬前置条件**
1. **本地学习资料库**：需要一套分学科、可检索的本地资料（教辅 / 试卷 / 讲义），桥接计划才有素材。库为空、或资料是无文字层的扫描件时，须先做 OCR 或建立路径索引。
2. **本地推理环境**：出题链路依赖本机已装 Ollama 并拉取 `qwen2.5:7b`（或等价本地模型）。无本地模型时出题环节失效，需改用其他出题来源。
3. **每日人力统筹**：五步闭环的第 ②③④⑤ 步（手写执行、三查、送批、对答案）须由家长 / 统筹人每日执行。无此角色，闭环断在中途。
4. **云端判读通道**：判读 / 批改需可用的云端模型访问渠道（账号 / 额度 / 成本由使用者自备）。

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

## 四、出题 / 判读链路（本地模型不判读）
- 本机 Ollama 装 `qwen2.5:7b`，**仅用于出题**，不判读。
- 判读 / 批改走云端模型。
- 调用示例：
  ```
  ollama run qwen2.5:7b "你是高中[科目]老师。基于以下知识点出 5 道循序渐进的题：[知识点]。要求：梯度由易到难，附答案与解析要点。"
  ```
- 细例见 `references/ollama_qgen.md`。

## 五、红线清单（逐条可勾选）
**进度 / 内容红线**
- [ ] 超前内容不提前拖入低周次（如高二下内容不进入高一进度）
- [ ] 英语读后续写以校情过关线为基线（如 75 词，非高考 150 词），严禁加量欠写
- [ ] 每篇三查必做、难篇必送批
- [ ] 概念卡点设独立「概念攻坚补充」附件隔离，攻破后再恢复闸门测试

**工具 / 数据红线**
- [ ] 本机模型只出题、不判读（判读走云端）
- [ ] 资料盘零丢失、永不自动删除、每批 ≤10、先清单再确认、同盘 move 可逆
- [ ] PDF 处理前先跑文字层预检，禁止默认「PDF 有文字」
- [ ] 对外交付文件一律脱敏，禁止出现任何内部代称

完整勾选表见 `references/redline_checklist.md`。

## 六、输出格式约定
- 单栏 HTML、顶部 TOC、零依赖可离线、可打印。
- 相对路径链接、well-formed 校验、旧版零残留。
- 交付前四闸门预检（控制层 / 内容源 / 格式核对 / 库缺口）见 `study-deliverable-precheck`。

## 七、关联
- 通用搭桥方法论已由 `study-plan-bridge` 覆盖，本 skill 只收专属部分（参数 + 红线 + 五步闭环 + 出题链路），通用部分引用即可，不重抄。
- 可选扩展模板见 `references/`：`daily_loop.md`（五步闭环 + 周任务单）、`redline_checklist.md`（红线勾选表）、`ollama_qgen.md`（本机出题链路细例）。
