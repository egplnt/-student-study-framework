---
name: student-study-framework
description: This skill should be used when building or maintaining a high-school student's study plan, bridging knowledge gaps (scan gaps → bridge), daily execution loops, weekly task sheets, or a local-LLM question-generation + cloud-grading pipeline. It encodes a reusable "scan gaps → bridge" methodology, a 5-step daily loop, an Ollama local question-generation setup, and a parameterized red-line checklist, generalized across students via replaceable parameters (subject / exam year / target band / main textbooks).
agent_created: true
---

# 学生学习工程框架（核心框架）

> 本 skill 已完全脱敏，使用中性示例表述，不依赖任何内部代称或代号。

## 何时使用
- 构建或维护高中生的学习计划、知识搭桥、周任务单、出题链路、红线校验时触发。
- 涉及「扫盲点→搭桥」方法论、每日闭环、本地模型出题 + 云端判读链路时触发。

## 一、核心定位（参数化，可套用不同学生）
以一个 2028 届「物化地」高考生为示例，框架对以下参数开放：
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

## 四、出题 / 判读链路（本地模型不判读）
- 本机 Ollama 装 `qwen2.5`，**仅用于出题**，不判读。
- 判读 / 批改走云端模型。
- 调用示例：
  ```
  ollama run qwen2.5 "你是高中[科目]老师。基于以下知识点出 5 道循序渐进的题：[知识点]。要求：梯度由易到难，附答案与解析要点。"
  ```

## 五、红线清单（逐条可勾选）
**进度 / 内容红线**
- [ ] 复合函数不许提前拖入低周次（属高二下内容）
- [ ] 英语读后续写以 75 词过关线为基线（非高考 150 词），严禁加量欠写
- [ ] 每篇三查必做、难篇必送批
- [ ] 概念卡点设独立「概念攻坚补充」附件隔离，攻破后再恢复闸门测试

**工具 / 数据红线**
- [ ] 本机 Ollama 只出题、不判读（判读走云端）
- [ ] 资料盘零丢失、永不自动删除、每批 ≤10、先清单再确认、同盘 move 可逆
- [ ] PDF 处理前先跑文字层预检，禁止默认「PDF 有文字」
- [ ] 对外交付文件一律脱敏，禁止出现任何内部代称

## 六、输出格式约定
- 单栏 HTML、顶部 TOC、零依赖可离线、可打印。
- 相对路径链接、well-formed 校验、旧版零残留。
- 交付前四闸门预检（控制层 / 内容源 / 格式核对 / 库缺口）见 `study-deliverable-precheck`。

## 七、关联
- 通用搭桥方法论已由 `study-plan-bridge` 覆盖，本 skill 只收专属部分（参数 + 红线 + 五步闭环 + 出题链路），通用部分引用即可，不重抄。
