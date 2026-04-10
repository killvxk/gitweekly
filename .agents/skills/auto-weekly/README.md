# Auto Weekly Skill - 快速开始

## 概述

将原 `auto_weekly.py` 的核心功能转换为 Claude Code skill，使用当前会话的 AI 能力替代付费的 Anthropic API，实现零成本的周报自动化生成。

## 文件结构

```
.claude/skills/auto-weekly/
├── SKILL.md                    # Skill 主文件
├── README.md                   # 本文件（快速开始）
├── references/                 # 详细文档
│   ├── script-api.md          # 脚本 API 文档
│   ├── description-rules.md   # 描述生成规则
│   └── troubleshooting.md     # 故障排除指南
└── scripts/                    # 配套脚本
    ├── cache_query.py         # 缓存查询
    └── cache_write.py         # 缓存写入
```

## 快速开始

### 触发 Skill

在 Claude Code 中说以下任何一句话：
- "生成周报"
- "处理文档链接"
- "更新 docs.md"

### 两种工作模式

**模式 1：全自动生成周报**
- 从 git 历史提取本周变更
- 自动生成周报文件到 `weekly/` 目录
- 自动提交到 git

**模式 2：处理源文件**
- 读取 markdown 文件中的 URL
- 生成中文描述（15-25 字）
- 转换为表格格式

## 核心优势

| 功能 | auto_weekly.py | auto-weekly skill |
|------|----------------|-------------------|
| AI 描述生成 | Anthropic API（付费） | Claude Code 会话（免费） |
| 成本 | 按 token 计费 | 零成本 |
| 维护性 | 单一大文件 | 模块化设计 |
| 易用性 | 命令行参数 | 交互式询问 |

## 配套脚本

### 快速使用

**查询缓存**：
```bash
python3 .claude/skills/auto-weekly/scripts/cache_query.py "<url>"
```

**写入缓存**：
```bash
python3 .claude/skills/auto-weekly/scripts/cache_write.py "<url>" "<description>"
```

**注意**：某些系统使用 `python` 而非 `python3`。详见 `references/script-api.md`。

## 描述生成规则

生成的中文描述必须符合：
- **长度**：15-25 字
- **格式**：`<核心功能>的<技术栈/领域>工具/库/框架`
- **要求**：简洁明了，突出核心功能

**示例**：
- ✓ "专为Windows 7系统定制的Go语言编译器"
- ✓ "支持120+协议的高性能服务指纹识别工具"
- ✗ "一个很棒的项目"

详细规则和示例请参考 `references/description-rules.md`。

## 使用示例

### 生成本周周报

```
用户: 生成本周的周报
Claude: [触发 auto-weekly skill]
        请确认参数：
        - 周报文件：weekly/2026-03-03_2026-03-09.md
        - 缓存文件：links_cache/descriptions_cache.json
        - 最多处理：50 个链接

        [开始处理...]

        ✓ 周报已生成：weekly/2026-03-03_2026-03-09.md
        📊 新增描述: 15
        📊 使用缓存: 8
        📊 删除无效: 2
```

### 处理源文件

```
用户: 更新 docs.md 中的链接描述
Claude: [触发 auto-weekly skill]
        [处理 docs.md 中的所有 URL...]

        ✓ 源文件处理完成
        📄 处理文件: docs.md
        📊 更新描述: 25
        📊 删除无效: 3
```

## 常见问题

### Python 命令不存在

某些系统使用 `python` 而非 `python3`。Skill 会自动检测可用命令。

详见：`references/troubleshooting.md`

### 缓存文件损坏

脚本会自动备份为 `.bak` 文件并重新创建。

详见：`references/troubleshooting.md`

### URL 抓取失败

会自动标记为 `__DELETED__` 并写入缓存，跳过该 URL。

详见：`references/troubleshooting.md`

## 详细文档

- **`SKILL.md`** - Skill 主文件，包含完整工作流程
- **`references/script-api.md`** - 脚本详细 API 文档和使用示例
- **`references/description-rules.md`** - 描述生成规则、格式要求和质量标准
- **`references/troubleshooting.md`** - 故障排除指南和常见问题解决

## 开发记录

- **日期**: 2026-03-08
- **转换来源**: `auto_weekly.py`
- **Skill 行数**: 约 1,500 字
- **脚本数量**: 2 个（cache_query.py, cache_write.py）
- **测试状态**: 全部通过 ✓

## 许可证

与项目主仓库保持一致
