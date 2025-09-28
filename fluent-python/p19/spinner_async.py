""" 
使用协程实现: 输出类似旋转指针对象的字符串表示形式和文本“Answer: 42”的文本
"""
import itertools
import time
from multiprocessing import Process, synchronize, Event
import asyncio
from primes import is_prime

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
    result = await slow() # await 驱动协程被调度
    spinner.cancel() # 取消协程, 如果是 asyncio.sleep 则会等待协程执行 3 秒后取消
    return result

async def slow() -> int:
    # time.sleep(3)
    # await asyncio.sleep(3)
    result = is_prime(5_000_111_000_222_021)  # 直接调用，不使用 await
    return 42

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
    