""" 
函数的类型提示: 泛化映射

MappingType[K, V] 表示一个泛化的映射， 其中 K 是键的类型， V 是值的类型
"""
import re
import sys
from collections.abc import Iterator, Mapping
import unicodedata
RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1

def tokenize(text: str) -> Iterator[str]:
    """ 返回全大些的单词构成的可迭代对象 """
    for match in RE_WORD.finditer(text):
        yield match.group().upper()

def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index



index = name_index(32, 65)
print(index['SIGN'])
print(index['DIGIT'])
print(index['DIGIT'] & index['EIGHT'])



