""" 
Python 私有属性和受保护的属性： 避免之类覆盖父类私有属性
"""
from Vector2d import Vector2d

v1 = Vector2d(3, 4)
print(v1.__dict__)
print(v1._Vector2d__x)
