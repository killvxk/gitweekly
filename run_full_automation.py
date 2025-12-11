#!/usr/bin/env python3
"""
直接运行完整自动化，无需交互输入
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
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "开始处理所有周报的描述" + " "*21 + "║")
    print("╚" + "="*58 + "╝")

    processor = AutoWeeklyProcessor(GIT_REPO_PATH)

    # 直接调用处理函数，不需要交互
    processor.process_existing_weeklies(max_links_per_week=50)

if __name__ == "__main__":
    main()
