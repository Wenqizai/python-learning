""" 
    拆包
"""
import os

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # 并行拆包

print(latitude)
print(longitude)

# 变量互换，省区中间值
a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

t = divmod(20, 8)
print(t)

# 参数前面加上一个 * 号，表示将元组中的每个元素都作为参数传递给函数
quotient, remainder = divmod(*t)
print(quotient, remainder)

# 丢弃不需要的变量
_, filename = os.path.split('/Users/wq/Documents/dev/code/Python/python-learning/fluent-python/p2/2-5-1.py')
print(filename)

print("--------------------------------")

# *args 捕获余下的任意数量的参数
a, b, *rest = range(5)
print(a, b, rest) # 0 1 2 [3, 4]  

a, b, *rest = range(3)
print(a, b, rest) # 0 1 [2]

a, b, *rest = range(2)
print(a, b, rest) # 0 1 []

# *args 可以应用到任意位置的变量，但是只能应用到一个变量上
a, *body, c, d = range(5)
print(a, body, c, d) # 0 [1, 2] 3 4

*head, b, c, d = range(5)
print(head, b, c, d) # [0, 1, 2] 3 4 5

