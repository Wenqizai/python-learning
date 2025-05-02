""" 
    导入类
"""
from electric_car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2019)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()