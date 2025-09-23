""" 
使用进程实现: 输出类似旋转指针对象的字符串表示形式和文本“Answer: 42”的文本
"""
import itertools
import time
from multiprocessing import Process, synchronize, Event

def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}' # 使用 ASCII 回车符（'\r'）把光标移到行头。
        print(status, end='', flush=True)
        if done.wait(.1):  # 如果其他线程设置了这个事件，则 Event.wait(timeout=None) 方法返回 True；经过 timeout 指定的时间后，返回 False。
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def slow() -> int:
    time.sleep(3)
    return 42

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
    