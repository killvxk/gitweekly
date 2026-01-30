# GSD (Get Shit Done) 中文帮助

GSD 是一个**元提示、上下文工程和规范驱动的开发系统**，专为 AI CLI（如 Claude Code）设计，解决**上下文腐烂**问题。

## 核心理念

GSD 通过结构化文件维护项目信息：
- `PROJECT.md` - 项目定义与需求
- `ROADMAP.md` - 里程碑与阶段规划
- `STATE.md` - 当前状态追踪

## 安装

```bash
npx get-shit-done-cc
```

更新到最新版本：
```bash
npx get-shit-done-cc@latest
```

---

## 标准工作流程

```
新项目 → 讨论阶段 → 规划阶段 → 执行阶段 → 验证工作 → 完成里程碑
```

| 步骤 | 命令 | 说明 |
|------|------|------|
| 1. 初始化 | `/gsd:new-project` | 定义需求和里程碑 |
| 2. 细化 | `/gsd:discuss-phase` | 捕获实现决策 |
| 3. 规划 | `/gsd:plan-phase` | 创建原子任务计划 |
| 4. 执行 | `/gsd:execute-phase` | 并行波次执行，每任务提交 |
| 5. 验证 | `/gsd:verify-work` | 手动用户验收测试 |
| 6. 归档 | `/gsd:complete-milestone` | 归档里程碑 |

---

## 命令详解

### 项目初始化

| 命令 | 说明 |
|------|------|
| `/gsd:new-project` | 深度上下文收集，生成 PROJECT.md 和路线图 |
| `/gsd:new-milestone` | 开始新里程碑周期，更新 PROJECT.md |
| `/gsd:map-codebase` | 分析现有代码库的技术栈、架构、约定和问题 |

### 阶段管理

| 命令 | 说明 |
|------|------|
| `/gsd:discuss-phase` | 规划前通过自适应提问收集阶段上下文 |
| `/gsd:list-phase-assumptions` | 暴露 Claude 对阶段实现方式的假设 |
| `/gsd:research-phase` | 研究如何实现某阶段（独立使用） |
| `/gsd:plan-phase` | 创建详细执行计划 (PLAN.md)，含验证循环 |
| `/gsd:execute-phase` | 基于波次的并行执行所有计划 |

### 路线图调整

| 命令 | 说明 |
|------|------|
| `/gsd:add-phase` | 在当前里程碑末尾添加阶段 |
| `/gsd:insert-phase` | 在现有阶段之间插入紧急工作（如 72.1） |
| `/gsd:remove-phase` | 移除未来阶段并重新编号 |
| `/gsd:plan-milestone-gaps` | 创建阶段以弥补里程碑审计发现的差距 |

### 验证与完成

| 命令 | 说明 |
|------|------|
| `/gsd:verify-work` | 通过对话式 UAT 验证已构建功能 |
| `/gsd:audit-milestone` | 归档前审计里程碑完成度 |
| `/gsd:complete-milestone` | 归档已完成里程碑，准备下一版本 |

### 会话管理

| 命令 | 说明 |
|------|------|
| `/gsd:pause-work` | 中途暂停时创建上下文交接 |
| `/gsd:resume-work` | 从上次会话恢复，完整上下文还原 |
| `/gsd:progress` | 检查项目进度，显示上下文，路由到下一步 |

### 快速任务

| 命令 | 说明 |
|------|------|
| `/gsd:quick` | 执行快速任务（bug修复、小功能），跳过可选代理 |
| `/gsd:add-todo` | 从当前对话上下文捕获想法或任务 |
| `/gsd:check-todos` | 列出待办事项并选择一个执行 |

### 调试

| 命令 | 说明 |
|------|------|
| `/gsd:debug` | 系统化调试，跨上下文重置保持状态 |

### 配置

| 命令 | 说明 |
|------|------|
| `/gsd:settings` | 配置 GSD 工作流开关和模型配置 |
| `/gsd:set-profile` | 切换 GSD 代理的模型配置（quality/balanced/budget） |
| `/gsd:update` | 更新 GSD 到最新版本并显示变更日志 |

### 其他

| 命令 | 说明 |
|------|------|
| `/gsd:help` | 显示可用 GSD 命令和使用指南 |
| `/gsd:join-discord` | 加入 GSD Discord 社区 |

---

## 模型配置

通过 `/gsd:set-profile` 切换：

| 配置 | 说明 |
|------|------|
| `quality` | 最高质量，使用最强模型 |
| `balanced` | 平衡质量与成本 |
| `budget` | 节省成本，使用轻量模型 |

---

## 文件结构

GSD 在项目中创建 `.planning/` 目录：

```
.planning/
├── PROJECT.md      # 项目定义
├── ROADMAP.md      # 里程碑路线图
├── STATE.md        # 当前状态
├── codebase/       # 代码库分析文档
├── quick/          # 快速任务追踪
└── phases/         # 各阶段计划
```

---

## 多代理编排

GSD 使用**精简编排器 + 专业代理**架构：

- 编排器负责调度和协调
- 专业代理执行具体任务（研究、规划、执行、验证）
- 每个代理使用新鲜上下文，避免上下文污染

---

## 典型使用场景

### 新项目

```
/gsd:new-project     # 初始化项目
/gsd:discuss-phase   # 讨论第一阶段
/gsd:plan-phase      # 规划实现
/gsd:execute-phase   # 执行计划
/gsd:verify-work     # 验证结果
```

### 现有代码库

```
/gsd:map-codebase    # 分析现有代码
/gsd:new-milestone   # 定义新里程碑
/gsd:plan-phase      # 规划阶段
```

### 快速修复

```
/gsd:quick           # 直接执行小任务
```

### 会话恢复

```
/gsd:resume-work     # 恢复上次进度
/gsd:progress        # 查看当前状态
```

---

## 参考

- GitHub: https://github.com/glittercowboy/get-shit-done
- 安装: `npx get-shit-done-cc`
