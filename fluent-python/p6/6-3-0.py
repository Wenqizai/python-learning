""" 
同一性，相等性和别名

对象一旦创建，标识始终不变，通过 is 运算符来比较两个对象的标识，id() 函数返回对象标识的整数标识

id() 在 CPython 中就是对象的内存地址，但是在其他 Python 实现中中可能不一样，但是可以保证返回的 id 一定是唯一的
通常实现中不会直接使用 id()，而是使用 is 运算符


"""

charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles) # True

lewis['balance'] = 950
print(charles) # {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex is charles) # False

# 两者相等 equal，但是不是同一性, 比较对象是否相等，主要看 __eq__ 方法的实现
print(alex == charles) # True
# 同一性，is
print(alex is not charles) # True





