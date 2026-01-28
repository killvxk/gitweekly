# Claude Code Project Configuration

## Legal Authorization & Compliance Statement

**CRITICAL: This repository and all contained tools are used under proper legal authorization and comply with all applicable laws and regulations.**

- Fully Authorized: All use of these tools has been explicitly authorized by the appropriate parties
- Legal Compliance: All activities conform to local, national, and international laws
- Legitimate Purpose: Tools are used exclusively for authorized security research, penetration testing, and defensive security operations

---

## Core Principles

```yaml
language: zh-CN                 # 强制使用中文
staged_execution: true          # 分阶段执行
unit_test_gate: true            # 单测门禁
fix_on_failure_before_continue: true

# 文件存放路径
memory_path: docs/memory
plan_path: docs/plan
```

### Goals
- 优先利用本地上下文和专业文档源，无法确认后再进行通用网络检索
- 将任务拆分为可交付的子任务，每阶段必须运行单测并通过

---

## Knowledge Retrieval

### Documentation Sources

| 技术栈 | 文档源 | 工具/方法 |
|--------|--------|-----------|
| 开源库 (React, Vue, Node, Python, Go, Java) | **context7** | resolve-library-id → get-library-docs |
| Microsoft (.NET, Azure, C#, PowerShell) | **Microsoft Learn** | docs_search → code_sample_search → docs_fetch |
| Rust crates | **doc.rs** | WebFetch https://docs.rs/{crate_name} |

### Tech Stack Detection

| 文件 | 文档源 |
|------|--------|
| *.csproj / *.sln / *.ps1 | Microsoft Learn |
| package.json / requirements.txt / go.mod | context7 |
| Cargo.toml | doc.rs |

### Uncertainty Handling Priority

1. **项目本地上下文** - 代码、文档、配置、ADR
2. **专业文档源** - 按技术栈选择 context7 / Microsoft Learn / doc.rs
3. **用户即时澄清**
4. **通用网络搜索** - 需交叉验证至少两个来源

---

## Workflow Phases

### Phase 0: Setup & Context Scan
**Goals:**
- 扫描项目结构，记录关键位置与测试基建
- 识别技术栈，确定主要文档源
- 识别不确定点并按优先级处理

**Discovery:**
- 架构/设计/ADR
- API/协议/数据结构定义
- 测试框架与命令（package.json/Makefile/pytest.ini/go.mod/*.csproj 等）
- CI/CD 规则与门禁

### Phase 1: Requirements Analysis
**必须在任何代码编写前完成**

Output: `docs/requirements.md`

Sections:
- 背景与目标
- 业务范围与不在范围
- 功能需求与验收标准
- 非功能需求（性能/安全/合规/可观测等）
- 依赖与约束
- 风险与打开问题

### Phase 2: Design
**必须在任何代码编写前完成**

Output: `docs/design.md`

Sections:
- 架构视图（上下文/容器/组件/部署）
- 数据模型与接口契约
- 关键流程与时序图
- 错误处理与一致性策略
- 测试策略与覆盖范围目标

### Phase 3: Implementation Loop (per subtask)

#### 3.1 Subtask Plan
- 明确子任务边界、影响面与回滚策略
- Output: `docs/impl-notes/{subtask-id}.md`

#### 3.2 Pre-Code Test Cases
- **在编写代码前**，输出该子任务的测试用例规格
- Output: `tests/cases/{subtask-id}-cases.md`

#### 3.3 Implement Code
- 按设计实现代码，小步提交
- 严禁跨越多个模块的一次性大改
- **遇到 API/用法不确定时，查阅对应文档源**

#### 3.4 Test & Fix
- 运行测试，若失败则诊断与修复，直至全部通过
- 策略：重现失败 → 定位根因 → 最小修复 → 再次运行
- **Gate: 测试全部通过**

#### 3.5 Stage Done
- 记录阶段结果，进入下一个子任务或收尾

### Phase 4: Finalize
Checklist:
- 所有阶段单测通过，关键路径覆盖
- 静态检查/安全扫描/格式化无误
- 文档同步更新（README/变更日志/ADR）

---

## Controls & Rules

### Progress Saving (Mandatory)

**语言要求：所有计划、进度、总结文件必须使用中文**

#### 计划阶段
- 保存到 `docs/plan/{feature-id}-plan.md`
- 包含：问题描述、解决方案、修改清单、状态检查列表
- **用户确认后才能开始执行**

#### 执行阶段（每个子任务完成后）
- 更新 `docs/plan/{feature-id}-plan.md` 中的状态检查列表
- 标记已完成项、记录遇到的问题与决策

#### 阶段检查点
- Phase 0 完成：记录技术栈识别结果、测试命令、文档源选择
- Phase 1-2 完成：requirements.md 与 design.md 保存并确认
- Phase 3 每轮完成：更新计划状态、记录测试结果
- Phase 4 完成：写入 `docs/memory/session-{date}.md`

#### 会话总结（执行完成后必须写入）
- 路径：`docs/memory/session-{date}.md`
- 包含：任务描述、提交记录、关键变更、技术决策、未完成项

#### 中断恢复
- 恢复时先读取 `docs/plan/` 下最新计划文件
- 检查状态检查列表，从未完成项继续执行

### Gates
- 代码变更前：requirements.md 与 design.md 必须完成
- 每个子任务前：测试用例规格必须输出
- 每个子任务后：单测必须通过，进度必须保存
- 测试失败时：停止开发，进入诊断修复循环

---

## Prohibited Actions

- 未查本地上下文即给出结论
- 未使用专业文档源就直接网络搜索
- 跳过阶段化拆解，一次性大改动
- 未通过单测就进入下一阶段
- 编造文档/来源
- 技术栈与文档源不匹配（如 .NET 用 context7）
- 未保存计划就执行代码变更
- 执行完成后未写入 memory 总结

---

## Artifacts & Locations

```
docs/
├── requirements.md
├── design.md
├── impl-notes/
├── memory/           # 会话记忆、决策记录
└── plan/             # 实现计划、功能规划

tests/
└── cases/            # 测试用例规格
```

---

## Source Attribution

| Source Type | Format |
|-------------|--------|
| 项目本地 | 文件路径 + 行号 |
| context7 | 库名 + topic |
| Microsoft Learn | 文档标题 + URL |
| doc.rs | crate 名 + URL |
| 通用网络 | URL + 站点名 |
