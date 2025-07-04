""" 
Tombola 虚拟子类

虚拟子类允许一个类视为另一个类的子类, 即使它们之间没有实际的继承关系
"""
import random
from tombola import Tombola

@Tombola.register # 注册为 Tombola 的虚拟子类
class TomboList(list): 

    def pick(self): 
        if self: 
            position = random.randrange(len(self))
            return self.pop(position)
        else: 
            raise LookupError('pop from empty TomboList')

    load = list.extend
    
    def loaded(self): 
        return bool(self)

    def inspect(self): 
        return tuple(sorted(self))

t = TomboList(range(5))
print(t)
print(issubclass(TomboList, Tombola))
print(issubclass(TomboList, list))