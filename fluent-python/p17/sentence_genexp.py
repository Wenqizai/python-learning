""" 
使用生成器表达式实现 Sentence 类
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        # 生成器表达式，懒加载生成
        return (match.group() for match in RE_WORD.finditer(self.text))

s = Sentence('"The time has come," the Walrus said,')
print(s)
