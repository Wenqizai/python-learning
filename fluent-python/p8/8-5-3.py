""" 
Optional 类型和 Union 类型

Union [] 至少需要有两个类型, 可以嵌套 Union[A, B, Uion[C, D, E]],
这个嵌套其实和 Union[A, B, C, D, E] 是等价的
"""
from typing import Optional, Union

# Optional[str] 表示 str 或 None
def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    pass

# Python 3.10 可以使用 | 表示 Union 类型, 连接多个 x | y | z
# 旧版本可以使用 Union[x, y, z] 表示 Union 类型
def show_count(count: int, singular: str, plural: str | None) -> str:
    pass

# 可以返回 Union 函数, 但是需要尽量避免, 给调用方带来额外的复杂性
def parse_token(token: str ) -> Union[str, float]:
    try: 
        return float(token)
    except ValueError:
        return token



