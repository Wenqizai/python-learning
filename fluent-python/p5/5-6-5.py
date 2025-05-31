""" 
@dataclass: 都柏林核心模式
"""
from dataclasses import dataclass, field, fields
from enum import Enum, auto
from datetime import date
from typing import Optional

class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()

@dataclass
class Resource:
    """ 描述媒体资源 """
    identifier: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date: Optional['date'] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __str__(self):
        return f"{self.title} by {', '.join(self.creators) if self.creators else 'Unknown Author'}"

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name}={value!r},')
        res.append(')')
        return '\n'.join(res)

    

description = 'Improving the design of existing code'
book = Resource(identifier='978-0-321-80352-4', title='The Art of Readable Code', creators=['Martin Fowler'], date=date(2010, 4, 1), type=ResourceType.BOOK, description=description)
print(book)     # 默认的 __str__
print("\n")
print(str(book)) # 默认的 __str__
print("\n")
print(repr(book)) # 默认的 __repr__





