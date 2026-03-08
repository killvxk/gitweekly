# Auto Weekly Skill - 使用说明

## 概述

这个 skill 将原 `auto_weekly.py` 的核心功能转换为 Claude Code skill，使用当前会话的 AI 能力替代付费的 Anthropic API，节省订阅成本。

## 文件结构

```
.claude/skills/auto-weekly/
├── SKILL.md                    # Skill 主文件（279行）
├── README.md                   # 本文件
└── scripts/
    ├── cache_query.py          # 缓存查询脚本
    └── cache_write.py          # 缓存写入脚本
```

## 核心功能

### 模式 1：全自动生成周报
从 git 历史检测本周变更 → 提取新增链接 → 生成 AI 描述 → 创建周报文件 → git 提交

### 模式 2：处理源文件
读取 docs.md、README.md 等文件 → 提取 URL → 生成 AI 描述 → 转换为表格格式

## 触发方式

当用户说以下任何一句话时，skill 会自动触发：
- "生成周报"
- "generate weekly report"
- "处理文档链接"
- "process document links"
- "更新 docs.md"
- "update docs.md"
- "GitHub 链接描述"
- 或提到处理 markdown 文件中的 URL

## 配套脚本说明

### 环境要求

脚本需要 Python 3.x。在不同系统中，Python 命令可能是 `python3` 或 `python`。

**检测可用命令**:
```bash
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "错误: 未找到 Python 解释器"
    exit 1
fi
```

后续示例中使用 `python3`，实际使用时应根据系统环境选择正确的命令。

### cache_query.py - 缓存查询

**功能**: 查询 URL 是否已有缓存描述

**用法**:
```bash
python3 .claude/skills/auto-weekly/scripts/cache_query.py "<url>" [--cache-file <path>]
```

**返回值**:
- 退出码 0: 找到缓存，输出描述
- 退出码 1: 未找到缓存（输出 `NOT_FOUND` 或 `DELETED`）
- 退出码 2: 错误（输出错误信息）

**示例**:
```bash
# 查询已存在的 URL
$ python3 .claude/skills/auto-weekly/scripts/cache_query.py \
    "https://github.com/XTLS/go-win7" \
    --cache-file links_cache/descriptions_cache.json
专为Windows 7系统定制的Go语言编译器

# 查询不存在的 URL
$ python3 .claude/skills/auto-weekly/scripts/cache_query.py \
    "https://github.com/nonexistent/repo" \
    --cache-file links_cache/descriptions_cache.json
NOT_FOUND
```

### cache_write.py - 缓存写入

**功能**: 写入或更新 URL 描述到缓存

**用法**:
```bash
python3 .claude/skills/auto-weekly/scripts/cache_write.py "<url>" "<description>" [--cache-file <path>]
```

**返回值**:
- 退出码 0: 写入成功
- 退出码 1: 写入失败

**特殊标记**:
- 使用 `__DELETED__` 作为描述，标记 URL 为已删除（404/失效）

**示例**:
```bash
# 写入新描述
$ python3 .claude/skills/auto-weekly/scripts/cache_write.py \
    "https://github.com/test/repo" \
    "测试仓库描述" \
    --cache-file links_cache/descriptions_cache.json
新增成功: https://github.com/test/repo

# 标记为已删除
$ python3 .claude/skills/auto-weekly/scripts/cache_write.py \
    "https://github.com/deleted/repo" \
    "__DELETED__" \
    --cache-file links_cache/descriptions_cache.json
新增成功: https://github.com/deleted/repo
```

## 工作流程示例

### 模式 1：全自动生成周报

1. 用户说："生成本周的周报"
2. Skill 询问确认参数（周报文件路径、缓存文件路径、最多处理链接数）
3. 计算本周日期范围（周一到周日）
4. 从 git 历史提取本周提交
5. 从 git diff 提取新增的 URL
6. 对每个 URL：
   - 调用 `cache_query.py` 检查缓存
   - 如果没有缓存，使用 WebFetch 抓取内容
   - 生成 15-25 字的中文描述
   - 调用 `cache_write.py` 写入缓存
7. 生成周报文件 `weekly/weekly-YYYY-MM-DD_YYYY-MM-DD.md`
8. 提交到 git

### 模式 2：处理源文件

1. 用户说："更新 docs.md 中的链接描述"
2. Skill 询问确认参数
3. 查找项目根目录下的 markdown 文件
4. 提取所有 URL
5. 对每个 URL：
   - 检查缓存
   - 生成描述
   - 写入缓存
6. 将 URL 列表转换为表格格式
7. 更新源文件

## 描述生成规则

生成的中文描述必须符合以下要求：
- 长度：15-25 字
- 格式：`<核心功能>的<技术栈/领域>工具/库/框架`
- 简洁明了，突出核心功能
- 使用中文，专有名词保留英文
- 避免空洞词汇（"强大的"、"优秀的"）

**示例**：
- ✓ "专为Windows 7系统定制的Go语言编译器"
- ✓ "基于Unicorn引擎的Windows二进制逆向调试仿真混合工具"
- ✓ "轻量级可嵌入式JavaScript引擎"
- ✗ "一个很棒的项目"

## 与原 Python 脚本的对比

| 功能 | auto_weekly.py | auto-weekly skill |
|------|----------------|-------------------|
| AI 描述生成 | Anthropic API（付费） | Claude Code 会话（免费） |
| 缓存管理 | 内置 Python 类 | 独立脚本（cache_query.py, cache_write.py） |
| 内容抓取 | requests + BeautifulSoup | WebFetch 工具 |
| Git 操作 | subprocess | Bash 工具 |
| 配置方式 | 命令行参数 | 交互式询问 |
| 可维护性 | 单一大文件 | 模块化（skill + 脚本） |

## 测试验证

脚本已通过以下测试：

1. **缓存查询测试**
   - 查询不存在的 URL → 返回 `NOT_FOUND`，退出码 1 ✓
   - 查询已删除的 URL → 返回 `DELETED`，退出码 1 ✓
   - 查询存在的 URL → 返回描述，退出码 0 ✓

2. **缓存写入测试**
   - 写入新 URL → 成功，退出码 0 ✓
   - 更新已有 URL → 成功，退出码 0 ✓
   - 写入删除标记 → 成功，退出码 0 ✓

3. **JSON 完整性测试**
   - 写入后 JSON 格式正确 ✓
   - 中文字符正确编码 ✓
   - 文件可被原 Python 脚本读取 ✓

## 注意事项

1. **速率限制**: 处理大量链接时，每个请求之间会延迟 1-2 秒
2. **缓存优先**: 始终先检查缓存，避免重复处理
3. **描述质量**: 确保生成的描述简洁、准确、符合中文表达习惯
4. **文件备份**: 更新文件前，建议先提交 git 或备份

## 故障排除

### 问题：脚本无法执行
```bash
chmod +x .claude/skills/auto-weekly/scripts/*.py
```

### 问题：缓存文件损坏
脚本会自动备份为 `.bak` 文件并重新创建

### 问题：URL 抓取失败
会自动标记为 `__DELETED__` 并写入缓存，跳过该 URL

## 未来改进方向

1. 支持更多 URL 类型（不仅限于 GitHub）
2. 添加批量重新生成描述的功能
3. 支持自定义描述模板
4. 添加描述质量评分机制
5. 支持多语言描述生成

## 许可证

与项目主仓库保持一致
