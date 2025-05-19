""" 
vector2d.py: 一个简单的类

向量相关运算：https://zhuanlan.zhihu.com/p/362035810

加法：

v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1 + v2)  # Vector(4, 5)

绝对值：

v = Vector(3, 4)
print(abs(v))  # ⎷(3 ^ 2 + 4 ^ 2) = 5.0

标量积：

print(v * 3)  # Vector(9, 12)
print(abs(v * 3))  # ⎷(9 ^ 2 + 12 ^ 2) = 15.0

"""

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # 开发者视角：提供完整信息，用于调试和开发
        # 应该尽可能包含重建对象所需的所有信息
        return f"Vector(x={self.x!r}, y={self.y!r})"
    
    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"    
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
