""" 
可切片的序列
"""
from vector_v1 import Vector

v1 = Vector([3, 4, 5])
print(len(v1))

print((v1[0], v1[-1]))

v7 = Vector(range(7))
print(v7[1:4])
