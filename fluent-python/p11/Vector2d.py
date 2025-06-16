""" 
向量类 Vector2d
"""
from array import array
from math import hypot, atan2, pi

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.__x!r}, {self.__y!r})"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))
        
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.__x) ^ hash(self.__y)
        
    def __abs__(self):
        return hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))
        
    def __format__(self, fmt_spec=''):
        return self.format(fmt_spec)

    def angle(self):
        return atan2(self.__y, self.__x)

    def format(self, fmt_spec=''):
        if fmt_spec.endswith('p'):  
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
        
v1 = Vector2d(3, 4)
print(v1.x, v1.y)

v1_clone = eval(repr(v1))
print(v1 == v1_clone)

