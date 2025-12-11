#!/usr/bin/env python3
"""
测试选项4：生成当前周的周报
"""
import sys
if sys.platform == 'win32':
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'ignore')
    except:
        pass

from auto_weekly import AutoWeeklyProcessor, GIT_REPO_PATH

def main():
    print("=" * 60)
    print("测试选项4：生成当前周的周报")
    print("=" * 60)

    processor = AutoWeeklyProcessor(GIT_REPO_PATH)

    # 测试生成当前周（不生成AI描述，设置max_links=0）
    processor.process_current_week(max_links=0)

if __name__ == "__main__":
    main()
