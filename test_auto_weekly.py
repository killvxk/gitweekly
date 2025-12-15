#!/usr/bin/env python3
"""
快速测试自动化周报功能
"""
import os
import sys
if sys.platform == 'win32':
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'ignore')
    except:
        pass

from pathlib import Path
from auto_weekly import WeeklyGenerator, DescriptionGenerator, WeeklyUpdater

def test_generation():
    """测试周报生成"""
    print("\n=== 测试1: 周报生成 ===")
    generator = WeeklyGenerator('f:/gitweekly')
    files = generator.generate_weekly_files('2025-07-21')
    print(f"✓ 生成/检查了 {len(files)} 个周报文件")
    return len(files) > 0

def test_description():
    """测试描述生成"""
    print("\n=== 测试2: 描述生成 ===")
    desc_gen = DescriptionGenerator(Path('f:/gitweekly/links_cache'))

    # 测试一个简单的链接
    test_url = "https://github.com/rust-lang/rust"
    print(f"测试链接: {test_url}")

    # 1. 获取内容
    print("  → 获取GitHub内容...")
    fetch_result = desc_gen.fetch_github_content(test_url)

    if fetch_result.status == "ok" and fetch_result.content:
        content = fetch_result.content
        print(f"  ✓ 成功获取内容 ({len(content)} 字符)")

        # 2. 生成描述
        print("  → 调用AI生成描述...")
        description = desc_gen.call_ai_for_summary(test_url, content[:1000])

        if description:
            print(f"  ✓ 生成描述: {description}")
            return True
        else:
            print("  ✗ AI调用失败")
            return False
    elif fetch_result.status == "not_found":
        print("  ✗ 仓库不存在/404")
        return False
    else:
        status = fetch_result.status
        http_status = fetch_result.http_status
        suffix = f" (HTTP {http_status})" if http_status else ""
        print(f"  ✗ 获取内容失败: {status}{suffix}")
        return False

def test_update():
    """测试周报更新"""
    print("\n=== 测试3: 周报更新 ===")
    updater = WeeklyUpdater(Path('f:/gitweekly/weekly'))

    # 找一个需要更新的文件
    weekly_files = sorted(Path('f:/gitweekly/weekly').glob('weekly-*.md'))

    for file_path in weekly_files[:3]:  # 只检查前3个
        links = updater.extract_links_needing_descriptions(file_path)
        if links:
            print(f"✓ {file_path.name}: 找到 {len(links)} 个需要描述的链接")
            print(f"  示例: {links[0]}")
            return True

    print("✓ 所有检查的文件都已完成")
    return True

def main():
    print("""
╔══════════════════════════════════════════╗
║     自动化周报工具 - 功能测试             ║
╚══════════════════════════════════════════╝
""")

    # 检查API Key
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("⚠️  ANTHROPIC_API_KEY 未设置，将跳过AI测试")

    results = {}

    # 测试1: 周报生成
    try:
        results['generation'] = test_generation()
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        results['generation'] = False

    # 测试2: 描述生成（需要API Key）
    if os.getenv('ANTHROPIC_API_KEY'):
        try:
            results['description'] = test_description()
        except Exception as e:
            print(f"✗ 测试失败: {e}")
            results['description'] = False
    else:
        results['description'] = None

    # 测试3: 周报更新
    try:
        results['update'] = test_update()
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        results['update'] = False

    # 总结
    print("\n" + "="*50)
    print("测试结果:")
    print("="*50)
    print(f"  周报生成: {'✓ 通过' if results['generation'] else '✗ 失败'}")
    if results['description'] is not None:
        print(f"  描述生成: {'✓ 通过' if results['description'] else '✗ 失败'}")
    else:
        print(f"  描述生成: - 跳过（无API Key）")
    print(f"  周报更新: {'✓ 通过' if results['update'] else '✗ 失败'}")
    print("="*50)

    all_passed = all(v for v in results.values() if v is not None)
    if all_passed:
        print("\n🎉 所有测试通过！脚本可以正常使用。")
    else:
        print("\n⚠️  部分测试失败，请检查错误信息。")

if __name__ == "__main__":
    main()
