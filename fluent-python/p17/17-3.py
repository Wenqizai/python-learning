""" 
序列可迭代的原因: iter 函数

内置函数 iter 执行以下操作。
01. 检查对象是否实现了 __iter__ 方法，如果实现了就调用它，获
取一个迭代器。
02. 如果没有实现 __iter__ 方法，但是实现了 __getitem__ 方
法，那么 iter() 创建一个迭代器，尝试按索引（从 0 开始）获
取项。
03. 如果尝试失败，则 Python 抛出 TypeError 异常，通常会提
示“'C' object is not iterable”（C 对象不可迭代），其
中 C 是目标对象所属的类。
"""
from collections.abc import Iterable

class Spam: 
    def __getitem__(self, index):
        print('->', index)
        raise IndexError()

spam_can = Spam()
print(iter(spam_can)) # 判断对象是否可以迭代，调用 iter 函数

print(list(spam_can))

print(isinstance(spam_can, Iterable))


class GooseSpam:
    def __iter__(self):
        pass

print(issubclass(GooseSpam, Iterable))

goose_spam = GooseSpam()
print(isinstance(goose_spam, Iterable))