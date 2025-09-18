""" 
惰性实现 Sentence 类

使用生成器函数 re.finditer, 避免一次性构建单词列表
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
        for match in RE_WORD.finditer(self.text):
            yield match.group()

s = Sentence('"The time has come," the Walrus said,')
print(s)

for word in s:
    print(word)