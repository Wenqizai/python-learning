""" 
注解: 仅限位置参数和变长参数

仅限位置函数: 
def tag(name, /, *content, class_=None, **attrs):
"""
from typing import Optional

def tag(
    name: str,
    /, # 仅限位置标识符, 左边必须为位置参数, 不能通过名字来传参
    *content: str, # * 表示 tuple 类型
    class_: Optional[str] = None,
    **attrs: str, # ** 表示 dict 类型
) -> str:
    ...

def tag(_name: str, *content: str, _class: Optional[str] = None, **_attrs: str) -> str:
    ...

# 调用 tag 函数
tag("h1", "hello", class_="sidebar")

