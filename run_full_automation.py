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

from auto_weekly import AutoWeeklyProcessor, get_config, logger

def main():
    logger.info("╔" + "="*58 + "╗")
    logger.info("║" + " "*15 + "开始处理所有周报的描述" + " "*21 + "║")
    logger.info("╚" + "="*58 + "╝")

    # 使用配置系统（自动从当前目录获取配置）
    config = get_config()
    processor = AutoWeeklyProcessor(config=config)

    # 直接调用处理函数，不需要交互
    processor.process_existing_weeklies()

if __name__ == "__main__":
    main()
