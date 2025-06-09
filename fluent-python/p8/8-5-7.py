""" 
类型提示: 抽象基类

博斯塔尔定律: 发送时要保守, 接受时要大方

函数方法定义可以用抽象的基类, 返回值需要具体类型
"""

from collections.abc import Mapping

# Mapping 是泛化的映射
def name2hex(name: str, color_map: Mapping[str, int]) -> str:
        pass

def tokenize(text: str) -> list[str]:
    """ 返回全大些的单词构成的列表 """
    return text.upper().split()



