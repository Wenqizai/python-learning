""" 
使用协程实现: 输出类似旋转指针对象的字符串表示形式和文本“Answer: 42”的文本

警告：主线程不能被暂停/挂起，否则协程也会被挂起

在 asyncio 创建的协程中千万不要使用 time.sleep()，除非想暂停整个程序。
如果希望协程空闲一段时间，什么也不做，那么应该使用 await asyncio.sleep()。

"""
import itertools
import time
from multiprocessing import Process, synchronize, Event
import asyncio

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}' # 使用 ASCII 回车符（'\r'）把光标移到行头。
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

async def supervisor() -> int:
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    spinner.cancel() # 取消协程, 如果是 time.sleep 则主线程和协程都被挂起，然后马上执行取消，导致协程的任务没有被执行
    return result

async def slow() -> int:
    time.sleep(3)
    return 42

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
    