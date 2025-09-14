""" 
重载向量加法运算符 +
"""

import itertools

class Vector:
    def __init__(self, components):
        self._components = list(components)
    
    def __iter__(self):
        return iter(self._components)
    
    def __add__(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)
        
    def __repr__(self):
        return f"Vector({self._components})"

# 相同长度的向量相加
v1 = Vector([3, 4, 5])
v2 = Vector([6, 7, 8])
print(v1 + v2)

# 不同长度的向量相加
v1 = Vector([3, 4, 5])
v2 = Vector([6, 7, 8, 9])
print(v1 + v2 )