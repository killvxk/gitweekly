# 脚本 API 文档

## Python 命令检测

在不同系统中，Python 命令可能是 `python3` 或 `python`。执行脚本前需要检测可用命令：

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

后续所有脚本调用使用 `$PYTHON_CMD` 变量。

## cache_query.py - 缓存查询

### 功能

查询 URL 是否已有缓存描述。

### 用法

```bash
$PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_query.py "<url>" [--cache-file <path>]
```

### 参数

- `url` (必需): 要查询的 URL
- `--cache-file` (可选): 缓存文件路径，默认为 `links_cache/descriptions_cache.json`

### 返回值

- **退出码 0**: 找到缓存，标准输出为描述内容
- **退出码 1**: 未找到缓存
  - 输出 `NOT_FOUND`: URL 不在缓存中
  - 输出 `DELETED`: URL 已标记为删除（404/失效）
- **退出码 2**: 发生错误，标准错误输出错误信息

### 示例

**查询存在的 URL**:
```bash
$ $PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_query.py \
    "https://github.com/XTLS/go-win7" \
    --cache-file links_cache/descriptions_cache.json
专为Windows 7系统定制的Go语言编译器
$ echo $?
0
```

**查询不存在的 URL**:
```bash
$ $PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_query.py \
    "https://github.com/nonexistent/repo" \
    --cache-file links_cache/descriptions_cache.json
NOT_FOUND
$ echo $?
1
```

**查询已删除的 URL**:
```bash
$ $PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_query.py \
    "https://github.com/deleted/repo" \
    --cache-file links_cache/descriptions_cache.json
DELETED
$ echo $?
1
```

### 在 Bash 中使用

```bash
# 检查缓存并根据结果采取行动
if description=$($PYTHON_CMD cache_query.py "$url" 2>/dev/null); then
    echo "使用缓存: $description"
else
    exit_code=$?
    if [ $exit_code -eq 1 ]; then
        echo "需要生成新描述"
    else
        echo "查询失败"
    fi
fi
```

## cache_write.py - 缓存写入

### 功能

写入或更新 URL 描述到缓存文件。

### 用法

```bash
$PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_write.py "<url>" "<description>" [--cache-file <path>]
```

### 参数

- `url` (必需): 要写入的 URL
- `description` (必需): URL 的描述
  - 使用 `__DELETED__` 标记 URL 为已删除（404/失效）
- `--cache-file` (可选): 缓存文件路径，默认为 `links_cache/descriptions_cache.json`

### 返回值

- **退出码 0**: 写入成功
- **退出码 1**: 写入失败

### 输出格式

成功时输出以下之一：
- `新增成功: <url>` - 新增 URL
- `更新成功: <url>` - 更新已有 URL

失败时输出错误信息到标准错误。

### 示例

**写入新描述**:
```bash
$ $PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_write.py \
    "https://github.com/test/repo" \
    "测试仓库描述" \
    --cache-file links_cache/descriptions_cache.json
新增成功: https://github.com/test/repo
```

**更新已有描述**:
```bash
$ $PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_write.py \
    "https://github.com/test/repo" \
    "更新后的描述" \
    --cache-file links_cache/descriptions_cache.json
更新成功: https://github.com/test/repo
```

**标记为已删除**:
```bash
$ $PYTHON_CMD .claude/skills/auto-weekly/scripts/cache_write.py \
    "https://github.com/deleted/repo" \
    "__DELETED__" \
    --cache-file links_cache/descriptions_cache.json
新增成功: https://github.com/deleted/repo
```

### 错误处理

脚本会自动处理以下情况：

1. **缓存文件不存在**: 自动创建目录和文件
2. **JSON 格式损坏**: 自动备份为 `.bak` 文件并重新创建
3. **写入权限问题**: 返回退出码 1 并输出错误信息

### 在 Bash 中使用

```bash
# 写入缓存并检查结果
if $PYTHON_CMD cache_write.py "$url" "$description" 2>/dev/null; then
    echo "缓存写入成功"
else
    echo "缓存写入失败"
    exit 1
fi
```

## 脚本实现细节

### 缓存文件格式

```json
{
  "https://github.com/user/repo": "仓库描述",
  "https://example.com/page": "页面描述",
  "https://deleted.com/404": "__DELETED__"
}
```

- 键：URL 字符串
- 值：描述字符串或 `__DELETED__` 标记
- 编码：UTF-8
- 格式：缩进 2 空格，`ensure_ascii=False`

### 特殊标记

- `__DELETED__`: 标记 URL 为已删除或失效
  - 查询时返回退出码 1，输出 `DELETED`
  - 避免重复尝试抓取失效 URL

### 错误码约定

- **0**: 成功
- **1**: 未找到 / 写入失败 / 已删除
- **2**: 系统错误（文件读取失败、JSON 解析失败等）

### 依赖

- Python 3.x
- 标准库：`json`, `argparse`, `pathlib`, `sys`
- 无第三方依赖

### 性能考虑

- 每次调用都会读取/写入完整的 JSON 文件
- 对于大量 URL（>1000），建议批量处理
- 缓存文件大小约为：`(URL长度 + 描述长度 + 10) * URL数量` 字节
