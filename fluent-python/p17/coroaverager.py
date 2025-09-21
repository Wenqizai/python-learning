""" 
定义一个计算累计平均值的协程
"""
from collections.abc import Generator

def averager() -> Generator[float, float, None]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

coro_avg = averager()
next(coro_avg)

print(coro_avg.send(10)) # 开始执行协程
print(coro_avg.send(30))
print(coro_avg.send(5))

coro_avg.close() # 终止协程
coro_avg.close()
coro_avg.send(5) # 终止之后不能 send