""" 
类型提示: Iterable
"""

from collections.abc import Iterable
from typing import TypeAlias
def fsum(_seq: Iterable[float]) -> float:
    """ 计算一个或多个数字的和 """
    return sum(_seq)

FromTo = tuple[str, str] # 类型别名
FromTo: TypeAlias = tuple[str, str] # 类型别名
def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text

l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0')]
text = 'mad skilled nood powned leet'
print(zip_replace(text, l33t))


