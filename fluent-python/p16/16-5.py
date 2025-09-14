""" 
重载标量乘法运算符 *
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
        
    def __mul__(self, scalar):
        return Vector(a * scalar for a in self)
            
    def __rmul__(self, scalar):
        return self * scalar
        
    def __repr__(self):
        return f"Vector({self._components})"


v1 = Vector([3, 4, 5])
print(v1 * 3)
print(11 * v1)