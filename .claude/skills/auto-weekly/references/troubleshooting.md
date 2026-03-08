# 故障排除指南

## 常见问题

### Python 命令不存在

**症状**:
```
bash: python3: command not found
```

**解决方案**:
1. 检测可用的 Python 命令：
```bash
command -v python3 || command -v python
```

2. 使用检测到的命令：
```bash
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
fi
```

3. 如果都不存在，安装 Python 3：
```bash
# Ubuntu/Debian
sudo apt install python3

# macOS
brew install python3
```

### 缓存文件损坏

**症状**:
```
JSONDecodeError: Expecting property name enclosed in double quotes
```

**解决方案**:
脚本会自动处理：
1. 备份损坏文件为 `.bak`
2. 创建新的空缓存文件
3. 继续执行

手动恢复（如果需要）：
```bash
# 查看备份
cat links_cache/descriptions_cache.json.bak

# 尝试修复 JSON
python3 -m json.tool links_cache/descriptions_cache.json.bak > fixed.json
```

### URL 抓取失败

**症状**:
```
WebFetch failed: timeout / 404 / connection error
```

**处理策略**:
1. 自动标记为 `__DELETED__`
2. 写入缓存
3. 跳过该 URL
4. 继续处理下一个

**手动重试**:
```bash
# 从缓存中删除失效标记
python3 -c "
import json
cache = json.load(open('links_cache/descriptions_cache.json'))
cache.pop('https://failed-url.com', None)
json.dump(cache, open('links_cache/descriptions_cache.json', 'w'), ensure_ascii=False, indent=2)
"
```

### Git 历史为空

**症状**:
```
本周没有提交记录
```

**原因**:
- 当前周（周一到周日）没有 git 提交
- 日期范围计算错误

**解决方案**:
1. 检查 git log：
```bash
git log --since="2026-03-03" --until="2026-03-09 23:59:59" --oneline
```

2. 如果确实没有提交，扩大日期范围或使用模式 2（处理源文件）

### 权限问题

**症状**:
```
Permission denied: /root/gitweekly/.claude/skills/auto-weekly/scripts/cache_write.py
```

**解决方案**:
1. 添加执行权限：
```bash
chmod +x .claude/skills/auto-weekly/scripts/*.py
```

2. 或使用 `python3` 显式调用：
```bash
python3 .claude/skills/auto-weekly/scripts/cache_write.py
```

### 描述质量不佳

**症状**:
- 描述过短或过长
- 信息不准确
- 包含空洞词汇

**解决方案**:
1. 检查 WebFetch 结果是否完整
2. 手动编辑描述：
```bash
python3 .claude/skills/auto-weekly/scripts/cache_write.py \
    "https://url" \
    "手动编写的更好描述"
```

3. 参考 `references/description-rules.md` 改进

## 错误处理策略

### 脚本退出码

| 退出码 | 含义 | 处理方式 |
|--------|------|----------|
| 0 | 成功 | 继续执行 |
| 1 | 未找到/失败 | 根据上下文决定（可能需要生成新描述） |
| 2 | 系统错误 | 停止执行，检查错误信息 |

### WebFetch 失败处理

```bash
# 伪代码
if webfetch_success:
    generate_description()
    write_to_cache()
else:
    write_to_cache(url, "__DELETED__")
    skip_url()
```

### 批量处理中断

如果处理大量 URL 时中断：
1. 已处理的 URL 已写入缓存
2. 重新运行时会跳过已缓存的 URL
3. 只处理剩余的 URL

**恢复方式**:
```bash
# 查看已处理数量
python3 -c "
import json
cache = json.load(open('links_cache/descriptions_cache.json'))
print(f'已缓存: {len(cache)} 个 URL')
"

# 继续处理（自动跳过已缓存）
# 重新运行 skill
```

## 性能优化

### 减少 WebFetch 调用

1. **使用缓存**：始终先检查缓存
2. **批量处理**：一次处理多个 URL，而非逐个运行
3. **限制数量**：使用 `--max-links` 参数

### 加速 git 操作

```bash
# 只获取必要的提交
git log --since="date" --until="date" --no-merges

# 只获取 diff 的新增行
git show <commit> --unified=0 --no-color | grep '^+'
```

### 缓存文件优化

对于大型缓存文件（>1000 URL）：
1. 定期清理失效 URL
2. 考虑使用数据库（SQLite）替代 JSON
3. 分片存储（按域名或日期）

## 调试技巧

### 启用详细日志

```bash
# 在脚本中添加调试输出
set -x  # 显示执行的命令
set -e  # 遇到错误立即退出
```

### 测试单个 URL

```bash
# 测试缓存查询
python3 cache_query.py "https://test-url.com"
echo "Exit code: $?"

# 测试缓存写入
python3 cache_write.py "https://test-url.com" "测试描述"
echo "Exit code: $?"

# 测试 WebFetch
# 在 Claude Code 中手动调用 WebFetch 工具
```

### 验证 JSON 格式

```bash
# 检查 JSON 是否有效
python3 -m json.tool links_cache/descriptions_cache.json > /dev/null
echo "JSON valid: $?"

# 格式化 JSON
python3 -m json.tool links_cache/descriptions_cache.json > formatted.json
mv formatted.json links_cache/descriptions_cache.json
```

## 最佳实践

### 1. 定期备份缓存

```bash
# 每次运行前备份
cp links_cache/descriptions_cache.json \
   links_cache/descriptions_cache.json.backup-$(date +%Y%m%d)
```

### 2. 分阶段处理

对于大量 URL：
1. 第一次运行：处理前 50 个
2. 检查质量
3. 调整描述规则
4. 继续处理剩余

### 3. 质量检查

```bash
# 检查描述长度分布
python3 -c "
import json
cache = json.load(open('links_cache/descriptions_cache.json'))
lengths = [len(desc) for desc in cache.values() if desc != '__DELETED__']
print(f'平均长度: {sum(lengths)/len(lengths):.1f}')
print(f'最短: {min(lengths)}, 最长: {max(lengths)}')
"
```

### 4. 增量更新

```bash
# 只处理新增的 URL
# skill 会自动跳过已缓存的 URL
```

## 联系支持

如果遇到无法解决的问题：
1. 检查 skill 版本是否最新
2. 查看 GitHub Issues
3. 提供详细的错误信息和复现步骤
