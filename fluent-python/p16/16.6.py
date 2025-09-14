""" 
把 @ 当作中缀运算符使用

@ 运算符支持的方法 __matmul__, __rmatmul__,  __imatmul__
"""

from math import e
from operator import le
from collections.abc import Sized, Iterable


class Vector:
    def __init__(self, components):
        self._components = list(components)
    
    def __iter__(self):
        return iter(self._components)
    
    def __len__(self):
        return len(self._components)

    def __matmul__(self, other):
        if (isinstance(other, Sized)) and (isinstance(other, Iterable)):
            if len(self) == len(other):
                return sum(a * b for a, b in zip(self, other))
            else:
                raise ValueError('@ requires vectors of the equal length')
        else:
            return NotImplemented
    
    def __rmatmul__(self, other):
        return self @ other



va = Vector([1, 2, 3])
vz = Vector([5, 6, 7])

print(va @ vz == 38.0)