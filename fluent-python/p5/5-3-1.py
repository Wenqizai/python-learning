""" 
典型的具名元组
"""
from collections import namedtuple
import json

print("-------------- 具名元组 ------------------")

# City 继承 tuple 的一些有用方法，__eq__, __lt__
City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

# 具名元组有 _fields 属性， 返回字段名
print(City._fields)

# 具名元组有 _make 方法， 可以接受一个可迭代对象来生成一个实例
print(City._make(('Beijing', 'CN', 12.3456, (116.4557, 39.9087))))

print("-------------- 具名元组转换成字典 ------------------")

Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict()) # ._asdict() 把具名元组转换成一个字典，如果需要保留顺序  OrderedDict(x._asdict())

print(json.dumps(delhi._asdict())) # 把字典转换成 json 字符串

print("------------- 具名元组指定默认字段 -------------------")

Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])

print(Coordinate(0, 0))
print(Coordinate(0, 0, 'NAD27'))
print(Coordinate._fields)
print(Coordinate._field_defaults)


