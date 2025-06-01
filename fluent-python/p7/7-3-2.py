""" 
高阶函数: map, filter, reduce
"""
from functools import reduce
from operator import add

def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)

# map 等同于以下
print(list(map(factorial, range(6))))
print([factorial(n) for n in range(6)])

print('\n')

# filter 等同于以下
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

print('\n')

# reduce 等同于以下
print(reduce(add, range(100)))
print(sum(range(100)))
