# -*- coding: utf-8 -*-
"""
为 Unit 01 ~ Unit 26 全量 26 个单元高效并发生成离线音频 MP3 与 PT 句级时间轴。
"""
import asyncio
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from gen_unit_audio import process_unit

UNIT_SEM = asyncio.Semaphore(2)

async def safe_process(u):
    async with UNIT_SEM:
        try:
            print(f"[开始] Unit {u:02d} 并发任务启动")
            await process_unit(u)
            print(f"[就绪] Unit {u:02d} 音频与 PT 时间轴已生成！")
        except Exception as e:
            print(f"[失败] Unit {u:02d} 处理出错: {e}")

async def main():
    start_u = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end_u = int(sys.argv[2]) if len(sys.argv) > 2 else 26

    print(f"=== 开始全量高效并发生成 Unit {start_u:02d} ~ Unit {end_u:02d} 的离线音频与 PT 时间轴 ===")
    tasks = [safe_process(u) for u in range(start_u, end_u + 1)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
