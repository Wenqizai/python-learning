""" 
用户定义的可调用类型
"""

import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())

print(bingo())         # 执行 bingo() 会调用 __call__ 方法
print(callable(bingo)) # 判断对象是否可调用使用内置函数 callable

