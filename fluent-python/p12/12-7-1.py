""" 
zip 函数: 将两个可迭代对象合并, 返回一个元组迭代器, 如果一个元组长度耗尽, 则不会继续遍历
"""
from itertools import zip_longest

print(zip(range(3), 'ABC')) # <zip object at 0x100671c80>

print(list(zip(range(3), 'ABC'))) # [(0, 'A'), (1, 'B'), (2, 'C')]

print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))) # [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2)]

# print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], strict=True))) # 报错, 严格模式下, 长度不一致会报错

# 不够补 fillvalue
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue='-1'))) # [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2), (-1, '-1', 3.3)]

print("-"*50)

a = [(1, 2, 3), (4, 5, 6)]
print(list(zip(*a))) # [(1, 4), (2, 5), (3, 6)]

b = [(1, 2), (3, 4), (5, 6)]
print(list(zip(*b))) # [(1, 3, 5), (2, 4, 6)]



