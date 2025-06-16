""" 
位置模式匹配
"""
from Vector2d import Vector2d

def keyword_pattern_demo(v: Vector2d):
    match v:
        case Vector2d(x=0, y=0):
            print(f'{v!r} is null')
        case Vector2d(x=0):
            print(f'{v!r} is vertical')
        case Vector2d(y=0) | Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x=x, y=y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')

keyword_pattern_demo(Vector2d(2, 0))
