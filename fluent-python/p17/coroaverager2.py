""" 
让协程返回一个值
"""
from typing import NamedTuple, Union
from collections.abc import Generator


class Result(NamedTuple):
    count: int # type: ignore
    average: float

class Sentinel:
    def __repr__(self): 
        return f'<Sentinel>'

STOP = Sentinel()

SendType = Union[float, Sentinel]

def averager2(verbose: bool = False) -> Generator[float, SendType, Result]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield # 返回 None
        if verbose:
            print('received: ', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

coro_avg = averager2()
next(coro_avg)
print(coro_avg.send(10)) # 返回 None
print(coro_avg.send(30))
print(coro_avg.send(5))

try: 
    print(coro_avg.send(STOP))
except StopIteration as e:
    print(e.value) # 居然通过捕获异常来获取返回值

print("===" * 20)


def compute():
    res = yield from averager2()
    print('computed: ', res)
    return res

comp = compute()
for v in [None, 10, 20, 30, STOP]:
    try:
        print(comp.send(v))
    except StopIteration as e:
        print(e.value)




