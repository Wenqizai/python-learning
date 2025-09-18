""" 
标准库中的生成函数: 合并多个可迭代对象的生成器函数
"""
import itertools

print("chain" + "==" * 10)

# chain(it1, ..., itN), 先产生 it1，然后产生 it2，最后产生 itN
print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))

print("chain.from_iterable" + "==" * 10)

# chain.from_iterable(it), 将 it 里面每一个元素先产生，一个接着一个，比如元组 [(0, 5),(1, 2)], 产生 [0, 5, 1, 2]
print(list(itertools.chain.from_iterable(enumerate('ABC'))))

print("zip" + "==" * 10)

# zip(it1, ..., itN), 将多个可迭代对象合并成一个可迭代对象，先后顺序，如果长度不一致，则以最短的长度为准
print(list(zip('ABC', range(5), [10, 20, 30, 40, 50])))

print("zip_longest" + "==" * 10)

# zip_longest(it1, ..., itN, fillvalue=None), 将多个可迭代对象合并成一个可迭代对象，先后顺序，如果长度不一致，则以最长的长度为准，不足的用 fillvalue 填充
print(list(itertools.zip_longest('ABC', range(5), fillvalue='-')))

print("product" + "==" * 10)

# product(it1, ..., itN), 计算笛卡尔积，返回元组数组，相当于多重循环的效果
print(list(itertools.product('ABC', range(2))))

suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits)))

print("==" * 10)

print(list(itertools.product('ABC'))) # [('A',), ('B',), ('C',)]

print("repeat" + "==" * 10)

# repeat=n, 重复 n 次
print(list(itertools.product('ABC', repeat=2)))
print(list(itertools.product('ABC', repeat=3)))

print("==" * 10)
rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
    print(row)
