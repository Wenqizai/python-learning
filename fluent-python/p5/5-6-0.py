""" 
@dataclass 装饰器

如果用户已经实现，则忽略该参数，用户优先

init: 是否生成 __init__ 方法
repr: 是否生成 __repr__ 方法
eq: 是否生成 __eq__ 方法
order: 是否生成 __lt__, __le__, __gt__, __ge__ 方法
unsafe_hash: 是否生成 __hash__ 方法
frozen: 是否让实例不可变

frozen=True 时，实例不可变，不能添加属性
frozen=False 时，实例可变，可以添加属性 (默认值)
"""

from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class DemoDataClass:
    a: int
