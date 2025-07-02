""" 
处理切片的 __getitem__ 方法
"""
from vector_v2 import Vector

v7 = Vector(range(7))
print(v7[-1])

print(v7[1:4])

print(v7[-1:])
