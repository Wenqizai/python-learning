""" 
Tombola 具体子类, 重写抽象方法, 并覆盖父类方法
"""
import random
from tombola import Tombola

class LotteryBlower(Tombola): 
    def __init__(self, iterable): 
        self._balls = list(iterable)

    def load(self, iterable): 
        self._balls.extend(iterable)

    def pick(self): 
        try: 
            position = random.randrange(len(self._balls))
        except ValueError: 
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self): 
        return bool(self._balls)

    def inspect(self): 
        return tuple(sorted(self._balls))

lotto = LotteryBlower(range(60))
print(lotto.inspect())
print(lotto.pick())
print(lotto.pick())