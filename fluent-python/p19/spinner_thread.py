""" 
使用线程实现: 输出类似旋转指针对象的字符串表示形式和文本“Answer: 42”的文本
"""
import itertools
import time
from threading import Thread, Event
from primes import is_prime

def spin(msg: str, done: Event) -> None: # done 参数的值是一个 threading.Event 实例， 一个用于同步线程的简单对象
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}' # 使用 ASCII 回车符（'\r'）把光标移到行头。
        print(status, end='', flush=True)
        if done.wait(.1):  # 如果其他线程设置了这个事件，则 Event.wait(timeout=None) 方法返回 True；经过 timeout 指定的时间后，返回 False。
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

    
def slow() -> int:
    # time.sleep(3)
    is_prime(5_000_111_000_222_021)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()


