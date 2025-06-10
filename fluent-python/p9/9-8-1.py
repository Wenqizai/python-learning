""" 
实现一个简单的装饰器: 改良后的 clock 装饰器

@functools.wraps(func) 本身也是一个装饰器, 作用是, 可以从原始函数 func 中复制所有的重要的元信息, __name__, __doc__, __module__ 等.

def clocked(*args, **kwargs), 增加了 **kwargs 参数, 可以接受任意数量的关键字参数. 比如可以输入 n = 6 作为接受参数. 而 * args 参数仅能够接受元组类型参数, 输入 n = 6 会报错 typeError.
"""
import time
import functools

def clock(func):
    
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        """ 显示函数的运行时间 """
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k}={v}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result}')
        return result
    
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n) -> int:
    """ 阶乘 """
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6)) 