""" 
不区分大小写的映射

混入类, 发挥作用, 在子类的方法解析顺序中, 必须排在前面
"""
import collections

def _upper(key):
    try: 
        return key.upper()
    except AttributeError:
        return key

class UpperCaseMixin:
    def __setitem__(self, key, value):
        super().__setitem__(_upper(key), value)

    def __getitem__(self, key):
        return super().__getitem__(_upper(key))

    def get(self, key, default=None):
        return super().get(_upper(key), default)

    def __contains__(self, key):
        return super().__contains__(_upper(key))

class UpperDict(UpperCaseMixin, collections.UserDict):
    pass

class UpperCounter(UpperCaseMixin, collections.Counter):
    """Specialized 'Counter' that uppercases keys."""

d = UpperDict([('a', 'letter A'), ('2', 'digit two')])
print(list(d.keys()))

d['b'] = 'letter B'
print('b' in d)

print(d['a'], d.get('B'))

print(list(d.keys()))