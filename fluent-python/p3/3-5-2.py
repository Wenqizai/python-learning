""" 
自动处理缺失的键

1. 普通 dict 获取 defaultdict
2. 实现 __missing__ 方法

"""

class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])

print(d['4'])

# print(d['1']) 缺失的值

print(d.get('2'))
print(d.get('4'))
print(d.get('1', 'N/A'))

print('2' in d)
print('1' in d)

print(2 in d)
print(1 in d)

print(d.get(2))

