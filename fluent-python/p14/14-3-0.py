""" 
子类化内置类型很麻烦 (不推荐内置类型的子类化)
"""
from collections import UserDict

class DoppleDict(dict):
    """ 子类化内置类型很麻烦 """

    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppleDict(one=1)
print(dd) # {'one': 1}
dd['two'] = 2
print(dd) # {'one': 1, 'h htwo': [2, 2]}

# dict 的 __init__ 和 __update__ 方法会忽略子类的 __setitem__ 方法
dd.update(three=3)
print(dd)

print("#" * 10 + "dict.update 会忽略 AnswerDict.__getitem__ 方法")

class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a='foo')
print(ad['a']) # 42

d = {}
d.update(ad)
print(d['a']) # foo
print(d) # {'a': 'foo'}

print("#" * 10 + "可以子类化 UserDict")

class DoppleDict2(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppleDict2(one=1)
print(dd) # {'one': 1}
dd['two'] = 2
print(dd) # {'one': 1, 'h htwo': [2, 2]}

dd.update(three=3)
print(dd)

class AnswerDict2(UserDict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict2(a='foo')
print(ad['a']) # 42

d = {}
d.update(ad)
print(d['a']) # 42
print(d) # {'a': 42}
