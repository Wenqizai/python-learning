""" 
super() 方法
"""

from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
    """ 按照更新顺序存储项 """

    def __init__(self, a, b):
        super().__init__() # Python 需要显式调用 super() 方法

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)

# 不推荐做法
class NotRecommended(OrderedDict):
    """ 这是一个反例 """

    def __init__(self, a, b):
        OrderedDict.__init__(self, a, b)

    def __setitem__(self, key, value):
        OrderedDict.__setitem__(self, key, value)
        self.move_to_end(key)

    
    