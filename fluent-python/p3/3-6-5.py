""" 
dict 的变体

子类映射应该继承 UserDict，而不是 dict， 因为 dict 的变体很多， 继承 dict 的话， 需要重写很多方法。

collections.UserDict 是一个包装类， 包装了 dict 的变体， 并提供了一些便利的方法。
"""

import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
        
        