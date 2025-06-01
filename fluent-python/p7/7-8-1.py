""" 
支持函数式编程的包: operator

1. operator 模块

2. functools 模块

"""
import operator
from functools import reduce
from operator import mul
from operator import itemgetter, attrgetter, methodcaller
from collections import namedtuple


# 没有使用 operator 模块
def factorial(n):
    """
    Return n!
    """
    return reduce(lambda a, b: a * b, range(1, n+1))

print(factorial(5))

def factorial_op(n):
    """
    Return n!
    """
    return reduce(mul, range(1, n+1))

print(factorial_op(5))


# operator 模块的 itemgetter 和 attrgetter 函数

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.775000)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.432639, -99.133209)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# itemgetter 多个索引函数, 构建返回元组
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

print("\n")

LatLon = namedtuple('LatLon', ['lat', 'lon'])
Metropolis = namedtuple('Metropolis', ['name', 'cc', 'pop', 'coord'])

metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))
               for name, cc, pop, (lat, lon) in metro_data]

print(metro_areas[0])
print(metro_areas[0].coord.lat)

# 使用 attrgetter 获取嵌套属性的值
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=name_lat):
    print(name_lat(city))


print("\n")


# operator 模块中所有函数的列表
print([name for name in dir(operator) if not name.startswith('_')])

print("\n")

# methodcaller 函数

s = 'The time has come'
upcase = methodcaller('upper') # 调用 str.upper 方法
print(upcase(s))


hyphenate = methodcaller('replace', ' ', '-')
print(hyphenate(s))  # 调用 str.replace 方法












