""" 
为 double 函数添加类型提示
"""
from fractions import Fraction
from typing import TypeVar, Protocol

print("#"*5 + "无类型提示")
def double(x):
    return x * 2
print(double(1.5))
print(double('A'))
print(double([10, 20, 30]))
print(double(Fraction(2, 5))) # 分数

print("#"*5 + "类型提示")

T = TypeVar('T')
class Repeatable(Protocol):
    def __mul__(self: T, repeat_count: int) -> T:
        ...

RT = TypeVar('RT', bound=Repeatable)
def double2(x: RT) -> RT:
    return x * 2

print(double2(1.5))
print(double2('A'))
print(double2([10, 20, 30]))
print(double2(Fraction(2, 5))) # 分数