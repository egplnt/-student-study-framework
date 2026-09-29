# student-study-framework

一套可复用的**高中生学习工程方法论 Skill**（适用于 WorkBuddy 智能体）。

## 简介
核心包含四块可复用资产：

1. **扫盲点 → 搭桥（scan gaps → bridge）**：定位知识跳跃点与概念卡点，为卡点设计桥接计划并设闸门测试。
2. **每日五步闭环**：生成打印清单 → 手写执行 → 90 秒三查 → 难篇送批 → 对答案报结果。
3. **本机 Ollama 出题 + 云端判读链路**：本地 `qwen2.5` 仅出题，判读 / 批改走云端。
4. **参数化红线清单**：进度 / 内容红线 + 工具 / 数据红线，逐条可勾选。

框架对参数开放（学段 / 科目 / 高考年份 / 目标分段 / 主线教辅），换一名学生仅替换参数即可复用。

## 安装

### 方式一：本地放置（推荐，零门槛）
将本仓库内容放到 WorkBuddy 用户级技能目录：

- **Windows**：`%USERPROFILE%\.workbuddy\skills\student-study-framework\`
- **macOS / Linux**：`~/.workbuddy/skills/student-study-framework/`

可直接 `git clone` 或下载 ZIP 解压，保证目录内含 `SKILL.md` 即可。重启 WorkBuddy 或在对话中提及本 skill 即触发。

### 方式二：WorkBuddy 官方技能市场
如需让陌生人也搜到，需走官方提交流程（审核后出现在「安装 skill」列表）。详见 WorkBuddy 官方文档。

## 使用
在对话中描述「制定学习计划 / 搭桥 / 周任务单 / 本地出题 / 红线校验」等需求，skill 会自动加载并引导流程。

## 脱敏说明
本 skill 为对外发布版本，所有内部代称与项目代号均已脱敏，使用中性示例表述，不含任何个人身份信息。

## 目录结构
```
student-study-framework/
├── SKILL.md        # 核心框架（自包含）
└── README.md       # 本文件
```
