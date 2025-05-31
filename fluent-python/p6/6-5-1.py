""" 
不要使用可变类型作为参数的默认值

# 使用默认值 [] 时，所有 HauntedBus 实例共享这个列表
# 如果实例化时没有传入乘客，使用默认值 []，意味着外部可以修改值
# 如果实例化时传入乘客，使用传入的列表，不会修改默认值 []

通常做法，参数列表使用默认参数 None, 然后检查是否为 None, 再进行初始化
"""

class HauntedBus:
    """ 一个受幽灵乘客折磨的校车 """
    def __init__(self, passengers=[]): # 如果没有传入乘客，使用默认值 []，意味着外部可以修改值
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers) # ['Alice', 'Bill']

bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers) # ['Bill', 'Charlie']

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers) # ['Carrie']

bus3 = HauntedBus()
print(bus3.passengers) # ['Carrie']

bus3.pick('Dave')
print(bus3.passengers) # ['Carrie', 'Dave']

print(bus2.passengers is bus3.passengers) # True

print(dir(HauntedBus.__init__))

print(HauntedBus.__init__.__defaults__) # (['Carrie', 'Dave'],) # 由于上面的赋值，所以默认值是 ['Carrie', 'Dave']


