""" 
数据类构建器概述

1. collections.namedtuple 和 typing.NamedTuple 构建都是 tuple 的子类
2. @dataclass 是类装饰器， 不影响类层次的构建
"""

from collections import namedtuple
import typing

class Coordinates:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


moscow = Coordinates(55.76, 37.62)
location =  Coordinates(55.76, 37.62)


print(moscow == location)
print((moscow.lat, moscow.lon) == (location.lat, location.lon))

print("--------------------------")

Coordinates = namedtuple('Coordinates', 'lat lon')
print(issubclass(Coordinates, tuple))

moscow = Coordinates(55.756, 37.617)
print(moscow)
print(moscow == Coordinates(55.756, 37.617))

print("--------------------------")

# typing 需要为各个字段添加类型注解
Coordinates = typing.NamedTuple('Coordinates', [('lat', float), ('lon', float)])
Coordinates = typing.NamedTuple('Coordinates', lat=float, lon=float)

print(issubclass(Coordinates, tuple))
print(typing.get_type_hints(Coordinates))

print("--------------------------")





