""" 
标准库中的装饰器:  functools.cache

1. functools.wraps(func)
2. functools.lru_cache(maxsize=128, typed=False)
3. functools.singledispatch
"""
import time
import functools

def clock(func):
    """ 显示函数的运行时间 """
    @functools.wraps(func)
    def clocked(*args, **kwargs):
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
def fibonacci(n) -> int:
    """ 斐波那契数列 """
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

# 缓存实现 func = clock(functools.cache(func))
@clock
@functools.cache
def cache_fibonacci(n) -> int:
    """ 斐波那契数列 """
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(fibonacci(6))
    print("-" * 40)
    print(cache_fibonacci(6))