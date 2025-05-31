""" 
为任意对象做浅拷贝和深拷贝

自定义的深拷贝，需要注意循环对象引用导致无限循环问题，deepcopy 会使用 memo 字典记录已经拷贝的对象，避免无限循环。   
"""
import copy

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)    


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1) # 浅拷贝
bus3 = copy.deepcopy(bus1) # 深拷贝

bus1.drop('Bill')

print(bus1.passengers)
print(bus2.passengers)
print(bus3.passengers)

print("\n")

# 循环引用的打印，b 引用了 a, a 引用了 b, 如果使用浅拷贝，会无限循环
a = [10, 20]
b = [a, 30]
a.append(b)

print(a) # [10, 20, [[...], 30]], 使用 [...], 表示自身，即 a 的循环引用
print(b) # [[10, 20, [...]], 30]，使用 [...] 表示自身，即 b 的循环引用

print("\n")

# 使用 deepcopy 深拷贝
c = copy.deepcopy(a)

print(c) # [10, 20, [[...], 30]]


