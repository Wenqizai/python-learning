""" 
数据类的构建
"""

from dataclasses import dataclass
from typing import NamedTuple
import typing

@dataclass(frozen=True)
class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat > 0 else 'S'
        ew = 'E' if self.lon > 0 else 'W'
        return f"{abs(self.lat):.1f}°{ns} {abs(self.lon):.1f}°{ew}"

# NamedTuple 出现在超类位置，但是它不是超类
# print(issubclass(Coordinate, typing.NamedTuple))
print(issubclass(Coordinate, tuple))






