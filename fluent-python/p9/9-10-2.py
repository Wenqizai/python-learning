""" 
参数化 clock 装饰器: 装饰器工厂
"""
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT): # 参数化装饰器工厂
    
    def decorate(func): # 真正的装饰器
        
        def clocked(*_args): # 包装被装饰的函数
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    
    return decorate

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)
        
    for i in range(3):
        snooze(.123)

    print("-" * 40)

    @clock('{name}: {elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

    print("-" * 40)

    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
    
    
    