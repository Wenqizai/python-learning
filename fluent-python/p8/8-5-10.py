""" 
类型提示: 静态协议

协议是指 typing.Protocol 的子类
"""
from typing import Protocol, Any, TypeVar, Sequence

class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        ...

LT = TypeVar('LT', bound=SupportsLessThan)
def top(series: Sequence[LT], length: int) -> list[LT]:
    return sorted(series, reverse=True)[:length]

print(top([4, 1, 5, 2, 6, 7, 3], 3))
l = 'mango pear apple kiwi banana'.split()
print(top(l, 3))

l2 = [(len(s), s) for s in l]
print(l2)
print(top(l2, 3))



