""" 
注解中可用的类型: 元组类型

元组类型注解分 3 种形式说明:

1. 用作记录元组
2. 带有具名字段, 用作记录的元组
3. 用作不可变序列的元组

"""
from geolib import geohash as gh
from typing import NamedTuple, Any, Sequence

# 1. 用作记录元组, 字段类型在 [] 内声明
# {'shanghai', 24.28, 'china'}, tuple[str, float, str]

PRECISION = 9
def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)

shanghai = 31.23, 121.4737 # 类型为 tuple[float, float]
print(type(shanghai)) # <class 'tuple'>
print(geohash(shanghai)) 

# 2. 带有具名字段, 用作记录的元组
# NamedTuple 是 Tuple 的子类的制造工厂， 与 tuple[float, float] 相容
class Coordinate(NamedTuple):
    lat: float
    lon: float

def geohash(lat_lon: Coordinate) -> str:
    return gh.encode(lat_lon.lat, lat_lon.lon, PRECISION)


def display(lat_lon: tuple[float, float]) -> str:
    lat, lon = lat_lon
    ns = 'N' if lat >= 0 else 'S'
    ew = 'E' if lon >= 0 else 'W'
    lat = abs(lat)
    lon = abs(lon)
    return f'{lat:.2f}°{ns}, {lon:.2f}°{ew}'

# 3. 用作不可变序列的元组
# tuple[int, ...] 表示 int 类型的元组，但是元组的元素不定
# stuff: tuple[Any, ...] 与 stuff: tuple 等价

def columnize(
        sequence: Sequence[str],
        num_columns: int = 0
    ) -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** 0.5)
    num_rows, reminder = divmod(len(sequence), num_columns)
    num_rows += bool(reminder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]


    
animals = 'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()
table = columnize(animals, 3)
print(table)

for row in table:
    print(' '.join(f'{word:10}' for word in row))


