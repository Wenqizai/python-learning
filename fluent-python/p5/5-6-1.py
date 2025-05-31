""" 
@dataclass: 字段选项

default_factory: 默认工厂函数, 可以指定函数， 类，其他调用对象
使用 field(default_factory=list), 可以让每一个 ClubMember 都实例化一个 list，而不是共用一个
"""
from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    # default_factory, 不允许加载 list class
    # guests: list = [] # ValueError: mutable default <class 'list'> for field guests is not allowed: use default_factory
    guests: list = field(default_factory=list)


@dataclass
class ClubStrMember:
    """ 
    list[str] 是泛型使用方法
    """
    name: str
    guests: list[str] = field(default_factory=list)


@dataclass
class ClubMemberWithDefault:
    """ 
    athlete: 默认值为 false, 但是不提供给 __repr__ 方法调用
    """
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)



