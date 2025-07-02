""" 
动态存取属性
"""
from vector_v3 import Vector

v = Vector(range(5))
print(v)
print(v.x)

v.x = 10 # 重写 setattr 方法, 不允许改写值
print(v.x)  

print(v) 