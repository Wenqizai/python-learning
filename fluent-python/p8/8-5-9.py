""" 
类型提示: 参数化泛型和 TypeVar
"""
from collections.abc import Sequence, Iterable
import random
from typing import TypeVar
from collections import Counter
from decimal import Decimal
from fractions import Fraction
from collections.abc import Hashable
T = TypeVar('T') # 类型变量, TypeVar 更加灵活, 没有让函数限定某种类型

def sample(population: Sequence[T], size: int) -> list[T]:
    """ 从 population 中随机选择 size 个元素 """
    if size < 1:
        raise ValueError('size must be >= 1')
    result = list(population)
    random.shuffle(result)
    return result[:size]

print(sample([1, 2, 3, 4, 5], 2))

def mode(data: Iterable[float]) -> float:
    pairs = Counter(data).most_common()
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]

# 灵活处理
def mode(data: Iterable[T]) -> T:
    pass


# 限定处理的 TypeVar
NumberT = TypeVar('NumberT', float, Decimal, Fraction)
def mode(data: Iterable[NumberT]) -> NumberT:
    pass

# 有界的 TypeVar, 限定类型 Hashable 及其子类
HashableT = TypeVar('HashableT', bound=Hashable)
def mode(data: Iterable[HashableT]) -> HashableT:
    pass


# 预定义的类型变量 AnyStr
AnyStr = TypeVar('AnyStr', str, bytes)
def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

print(concat('abc', 'def'))
print(concat(b'abc', b'def'))





