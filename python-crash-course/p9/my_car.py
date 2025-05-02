""" 
    导入类
"""
from electric_car import Car, ElectricCar # 导入car.py中的Car 和 ElectricCar 类
import electric_car # 导入整个 car 模块


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_leaf = ElectricCar('nissan', 'leaf', 2019)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()