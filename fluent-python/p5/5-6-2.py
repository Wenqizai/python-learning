""" 
@dataclass: 初始化后处理

__post_init__: 初始化后处理, 在 __init__ 之后调用
"""
from dataclasses import dataclass, field
from typing import ClassVar
@dataclass
class ClubMember:
    name: str
    # default_factory, 不允许加载 list class
    # guests: list = [] # ValueError: mutable default <class 'list'> for field guests is not allowed: use default_factory
    guests: list = field(default_factory=list)
    
@dataclass
class HackerClubMember(ClubMember):
    all_handles: ClassVar[set] = set() # @dataclass: 带类型的类属性
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            # 如果 handle 已经存在，则抛出异常
            raise ValueError(f'handle {self.handle} already exists')
        cls.all_handles.add(self.handle)

        

anna = HackerClubMember('Anna Ravenscroft', handle='AnnaRaven')
print(anna)

leo = HackerClubMember('Leo Rochael', handle='leo')
print(leo)

leo2 = HackerClubMember('Leo Rochael', handle='leo')
print(leo2)