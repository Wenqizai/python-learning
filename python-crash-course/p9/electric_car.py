""" 
    继承
"""
from car import Car


""" 
    电动车继承汽车类
"""
class ElectricCar(Car):
    """ 电动汽车的独特之处 """
    
    def __init__(self, make, model, year):
        """ 初始化父类的属性 """
        super().__init__(make, model, year)
        """ 子类特有的属性 """
        self.battery_size = 75
        
    def describe_battery(self):
        """ 打印一条描述电池容量的消息 """
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self, gas):
        """ 电动车没有油箱 """
        print("This car doesn't need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.read_odometer()
my_tesla.increment_odometer(100)
my_tesla.read_odometer()


my_tesla.describe_battery()
my_tesla.fill_gas_tank(10)


class Battery:
    """ 一次模拟电动汽车电池的简单尝试 """
    
    def __init__(self, battery_size=75):
        """ 初始化电池的属性 """
        self.battery_size = battery_size
        
    def describe_battery(self):
        """ 打印一条描述电池容量的消息 """
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """ 打印一条消息，指出电池的续航里程 """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCar(Car):
    """ 电动汽车的独特之处 """
    
    def __init__(self, make, model, year):
        """ 初始化父类的属性 """
        super().__init__(make, model, year)
        # 这里定义了一个电池类，相当于组合进了电动汽车类
        self.battery = Battery()
        
my_leaf = ElectricCar('nissan', 'leaf', 2019)
print(my_leaf.get_descriptive_name())

# 访问组合类的方法
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
        