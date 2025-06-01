""" 
把函数视为对象
"""

def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial(42))

print(factorial.__doc__)

print(type(factorial))

fact = factorial

print(fact)
print(fact(5))

print(map(fact, range(11)))
print(list(map(fact, range(11)))) # 使用 map 和 factorial 函数, 计算 0 到 10 的阶乘

