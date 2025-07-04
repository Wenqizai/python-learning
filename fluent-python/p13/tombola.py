""" 
Tombola 抽象基类
包含 2 个抽象方法, 以及 2 个具体方法
"""
import abc
import random

class Tombola(abc.ABC): 
    @abc.abstractmethod
    def load(self, iterable): 
        """ 从可迭代对象中添加元素 """

    @abc.abstractmethod
    def pick(self): 
        """ 
        随机删除元素, 并返回被删除的元素
        如果实例为空, 那么这个方法应该抛出 LookupError
        """

    def loaded(self): 
        """ 如果至少有一个元素, 那么返回 True, 否则返回 False """
        return bool(self.inspect())

    def inspect(self): 
        """ 返回由容器中的当前元素构成的有序元组 """
        items = []
        while True: 
            try: 
                items.append(self.pick())
            except LookupError: 
                break
        self.load(items)
        return tuple(sorted(items))

class BingoCage(Tombola): 
    def __init__(self, items): 
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items): 
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

# bingo = BingoCage() # 实例化报错, 没有实现抽象方法
# print(bingo.pick())
# print(bingo.pick())