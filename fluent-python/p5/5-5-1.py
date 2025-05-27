""" 
类型提示：运行时没有作用

类型提示可以提供给第三方类型检查工具，如 mypy 和 pycharm， 这些工具可以静态分析
"""
import typing

class Coordinates(typing.NamedTuple):
    lat: float
    lon: float

trash = Coordinates('Ni!', 78.9101)
print(trash)

# 类型提示在运行时没有作用
print(trash.lat)
print(trash.lon)
