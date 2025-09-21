""" 
返回一个产生字符串元组的迭代器
"""
from collections.abc import Iterable

FromTo = tuple[str, str]

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text

if __name__ == '__main__':
    # Thant wans an test， 原因 a 全部被替换成 an
    print(zip_replace('This is a test', [('This', 'That'), ('is', 'was'), ('a', 'an')]))
