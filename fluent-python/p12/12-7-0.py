""" 
哈希和快速等值测试
"""
import functools
import operator

reduce = 2 * 3 * 4 * 5
reduce2 = functools.reduce(lambda a, b: a * b, range(1, 6))
print(reduce == reduce2)

n = 0
for i in range(1, 6):
    n ^= i
print(n)
print(functools.reduce(lambda a, b: a ^ b, range(6)))
print(functools.reduce(operator.xor, range(6)))