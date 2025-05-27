""" 
带类型的具名元组
"""
from collections import namedtuple
from typing import NamedTuple

# 每个字段都带类型
class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'

print(Coordinate(12.3456, 78.9101))
print(Coordinate(12.3456, 78.9101, 'NAD27'))