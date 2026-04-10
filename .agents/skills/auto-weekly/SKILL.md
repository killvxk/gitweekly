---
name: auto-weekly
description: This skill should be used when the user asks to generate weekly reports from git history, process document links, update markdown files with URL descriptions, or mentions "生成周报", "处理文档链接", "更新 docs.md". Automates weekly report generation by extracting URLs from git commits or source files, generating concise Chinese descriptions, and organizing them into markdown tables.
---

# Auto Weekly - 自动化周报生成

复刻 `auto_weekly.py` 的核心功能，使用 Codex 当前会话替代 Anthropic API，节省订阅成本。

## 两种工作模式

### 模式 1：全自动生成周报
从 git 历史检测本周变更 → 提取新增链接 → 生成 AI 描述 → 创建周报文件 → git 提交

### 模式 2：处理源文件
读取 docs.md、README.md 等文件 → 提取 URL → 生成 AI 描述 → 转换为表格格式

## 环境要求

### Python 命令检测

在执行脚本前，检测系统中可用的 Python 命令：

```bash
# 检测 python3 或 python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "错误: 未找到 Python 解释器"
    exit 1
fi
```

后续所有 `python3` 命令应替换为 `$PYTHON_CMD`。

**注意**: 本文档中的示例使用 `python3`，实际执行时应根据系统环境使用正确的命令。

## 使用流程

### 启动时询问

询问用户选择模式：

```
请选择运行模式：
1. 全自动生成周报（从 git 历史）
2. 处理源文件（docs.md 等）

请输入选项 (1/2):
```

然后询问：
- 最多处理链接数（默认：50）
- 缓存文件路径（默认：`links_cache/descriptions_cache.json`）

---

## 模式 1：全自动生成周报

### 步骤 1：计算当前周范围

获取本周一到周日的日期。输出：`📅 周期: 2026-03-03 ~ 2026-03-09`

### 步骤 2：获取本周 git 提交

执行：
```bash
git log --since="2026-03-03" --until="2026-03-09 23:59:59" --pretty=format:"%H|%an|%ae|%ad|%s" --date=iso
```

解析输出，提取提交信息。如果没有提交，提示"本周没有提交记录"并结束。

### 步骤 3：从 git diff 提取新增链接

对每个提交执行：
```bash
git show <commit_hash> --unified=0 --no-color
```

从 diff 输出中提取：
- 以 `+` 开头的行（新增内容）
- 匹配 URL 正则：`https?://[^\s<>"{}|\\^`\[\]]+`
- 提取文件名（从 `diff --git a/xxx b/xxx` 行）

按文件分组存储：`{filename: [url1, url2, ...]}`

### 步骤 4：筛选需要生成描述的 URL

对每个 URL：
1. 调用缓存查询脚本检查是否已有描述
2. 如果有描述且有意义（不是 URL 本身、不是"无"），跳过
3. 否则加入待处理列表

### 步骤 5：生成 AI 描述

对每个待处理的 URL：

#### 5.1 检查缓存
```bash
$PYTHON_CMD .Codex/skills/auto-weekly/scripts/cache_query.py "<url>"
```
- 退出码 0：使用缓存
- 退出码 1：继续生成

**注意**: 使用 `$PYTHON_CMD` 变量（在环境要求部分检测），而非硬编码 `python3`。

#### 5.2 抓取内容

**GitHub URL：**
使用 WebFetch 获取：
```
url: https://github.com/<owner>/<repo>
prompt: 提取这个 GitHub 仓库的 README 内容、项目描述和主要特性。重点关注：1) 项目是什么 2) 核心功能 3) 技术栈
```

**普通网页：**
使用 WebFetch 获取：
```
url: <url>
prompt: 提取这个网页的标题、主要内容和核心信息
```

如果抓取失败（404、超时等），标记为 `__DELETED__` 并写入缓存。

#### 5.3 生成中文描述

基于抓取的内容，生成 15-25 字的中文描述。

**描述要求：**
- 简洁明了，突出核心功能
- 使用中文，专有名词保留英文
- 格式：`<核心功能>的<技术栈/领域>工具/库/框架`
- 避免空洞词汇（"强大的"、"优秀的"）

**示例：**
- ✓ "专为Windows 7系统定制的Go语言编译器"
- ✓ "基于Unicorn引擎的Windows二进制逆向调试仿真混合工具"
- ✗ "一个很棒的项目"

**生成步骤：**
1. 识别项目的核心功能
2. 提取技术栈和应用领域
3. 组合成简洁描述
4. 确保长度 15-25 字

#### 5.4 写入缓存
```bash
$PYTHON_CMD .Codex/skills/auto-weekly/scripts/cache_write.py "<url>" "<description>"
```

**注意**: 使用 `$PYTHON_CMD` 变量，而非硬编码 `python3`。

**速率控制：** 每处理一个 URL 后，延迟 1-2 秒。

### 步骤 6：生成周报文件

创建文件：`weekly/weekly-<week_start>_<week_end>.md`

**文件格式：**
```markdown
# Weekly Report: <week_start> ~ <week_end>

## <分类1>（如 docs.md）

| 链接 | 描述 |
|------|------|
| [项目名](url) | 生成的描述 |
```

**分类规则：**
- 按文件名分组
- 每个分类一个表格
- 链接按添加顺序排列

### 步骤 7：git 提交

```bash
git add weekly/weekly-<week_start>_<week_end>.md
git add links_cache/descriptions_cache.json
git commit -m "docs: 生成周报 <week_start> ~ <week_end>

Co-Authored-By: Codex Opus 4.6 <noreply@anthropic.com>"
```

### 步骤 8：输出总结

```
✓ 全自动模式完成！

📄 周报文件: weekly/weekly-2026-03-03_2026-03-09.md
📊 新增描述: 15
📊 删除无效链接: 2
📊 使用缓存: 8
```

---

## 模式 2：处理源文件

### 步骤 1：获取源文件列表

查找项目根目录下的源文件：
```bash
find . -maxdepth 1 -type f \( -name "*.md" -o -name "*.txt" \) ! -name "README.md" ! -path "./weekly/*"
```

如果没有找到，提示"未找到需要处理的源文件"并结束。

### 步骤 2：提取 URL

对每个文件，使用 Read 工具读取内容，提取所有 URL。

**正则表达式：** `https?://[^\s<>"{}|\\^`\[\]]+`

**过滤规则：**
- 排除常见无效 URL
- 排除已在表格中的 URL

### 步骤 3：生成描述

与模式 1 的步骤 5 相同：检查缓存 → 抓取内容 → 生成描述 → 写入缓存

### 步骤 4：更新源文件为表格格式

**转换规则：**

原格式：
```markdown
- [项目名](url)
- url
```

转换为表格：
```markdown
| 链接 | 描述 |
|------|------|
| [项目名](url) | 生成的描述 |
```

**处理逻辑：**
1. 找到文件中所有 URL 列表区域
2. 将每个 URL 转换为表格行
3. 如果 URL 标记为 `__DELETED__`，从文件中删除
4. 使用 Edit 工具更新文件

### 步骤 5：输出总结

```
✓ 源文件处理完成！

📄 处理文件: docs.md, C2.md
📊 更新描述: 25
📊 删除无效链接: 3
```

---

## 附加资源

### 参考文档

详细信息请查阅：
- **`references/script-api.md`** - 脚本完整 API 文档和使用示例
- **`references/description-rules.md`** - 描述生成规则、格式要求和质量标准
- **`references/troubleshooting.md`** - 故障排除指南和常见问题解决

### 配套脚本

- **`scripts/cache_query.py`** - 查询 URL 缓存描述
- **`scripts/cache_write.py`** - 写入或更新 URL 描述到缓存

详细用法请参考 `references/script-api.md`。
