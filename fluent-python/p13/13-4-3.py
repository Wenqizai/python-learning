""" 
快速失败
"""
from typing import Union, Iterable

# 构造序列
def __init__(self, iterable): 
    self._fields = tuple(iterable)

# 验证合法性
field_names = 'name age'
try:
    field_names = field_names.replace(',', '').split()
except AttributeError: 
    pass
field_names = tuple(field_names)
# isidentifier 判断是否是合法的标识符
if not all(s.isidentifier() for s in field_names): 
    raise ValueError('field names must be valid identifiers')

# 类型声明
def namedtuple(
      typename: str,
      field_names: Union[str, Iterable[str]],
    ):
    ...