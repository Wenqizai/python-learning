""" 
    类
    1. 类名应该使用大写字母开头，如 Dog
    2. 类名中不要使用下划线，如 dog_class
    3. 类定义后面紧跟一个文档字符串，用于描述类的功能
    
    __init__() 方法
    
    1. __init__() 方法是一个特殊的方法，用于初始化类的属性
    2. __init__() 约定两个 __，如果没有则不会被调用, 这个约定是避免与其他方法冲突
    3. 形参 self 必不可少，且必须位于其他形参前面, __init__() 调用时会自动传入 self，可以通过 self 访问类的属性和方法
    
    
    
    
"""

class Dog:
    """ 一次模拟小狗的简单尝试 """
    
    def __init__(self, name, age):
        """ 初始化属性 name 和 age """
        self.name = name
        self.age = age

    def sit(self):
        """ 模拟小狗被命令时蹲下 """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ 模拟小狗被命令时打滚 """
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

# 属性访问
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# 方法调用
my_dog.sit()
my_dog.roll_over()

print("--------------------------------")

# 创建多个实例
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

