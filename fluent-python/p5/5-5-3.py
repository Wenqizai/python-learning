""" 
类型提示：变量注解的意义
"""
import typing
from dataclasses import dataclass

class DemoPlainClass:
    a: int         # 注解
    b: float = 1.1 # 注解 + 属性
    c = 'spam'     # 属性

print(DemoPlainClass.__annotations__)

# 没有绑定属性值，不能访问
# print(DemoPlainClass.a) # AttributeError: type object 'DemoPlainClass' has no attribute 'a'

print(DemoPlainClass.b)
print(DemoPlainClass.c)
# print(DemoPlainClass.__dict__)

print("------------- 元组 NamedTuple ------------------")

# typing.NamedTuple 创建类属性 a 和 b，c 是普通类的属性
class DemoNTClass(typing.NamedTuple):
    a: int          # 注解 + 属性
    b: float = 1.1  # 注解 + 属性
    c = 'spam'      # 属性

print(DemoNTClass.__annotations__)
print(DemoNTClass.a)
print(DemoNTClass.b)
print(DemoNTClass.c)
print(DemoNTClass.__doc__)
# print(DemoNTClass.__dict__)

# 创建实例, 可传入 a, b. 其中 b 有默认值可以不传
nt = DemoNTClass(1, 2.2)
print(nt)
print(nt.a)
print(nt.b)
print(nt.c)
print(nt.__doc__)

# 创建实例, 只传入 a
nt = DemoNTClass(1)
print(nt)
print(nt.a)
print(nt.b)
print(nt.c)

print("------------- dataclass ------------------")

# 使用 dataclass 装饰器创建类，实例是可变的，运行时不检查类型
@dataclass
class DemoDataClass:
    a: int  # 注解
    b: float = 1.1
    c = 'spam'

print(DemoDataClass.__annotations__)
print(DemoDataClass.__doc__)
print(DemoDataClass.b)
print(DemoDataClass.c)
# print(DemoDataClass.a) AttributeError: type object 'DemoDataClass' has no attribute 'a'

dc = DemoDataClass(9)
print(dc)
print(dc.a)
print(dc.b)
print(dc.c)
dc.c = 'whatever'
# 不存在属性也可以加进去
dc.z = 'secret'
print(dc.z)


