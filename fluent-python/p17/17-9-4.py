""" 
标准库中的生成函数: 用于重新排列元素的生成器函数
"""
import itertools

print("groupby" + "==" * 10)

# groupby(it, key=None), 产出 (key, group) 形式的二元组，其中 key 是分组标准，group 是生成器，用于产出分组内的项
print(list(itertools.groupby('LLLLAAGGG')))

for char, group in itertools.groupby('LLLLAAGGG'):
    print(char, "->", list(group))

print("sorted" + "==" * 10)
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals)

for length, group in itertools.groupby(animals, len):
    print(length, "->", list(group))

print("reverse" + "==" * 10)

# reversed(seq), 倒序产出 seq 中的项，seq 必须是序列，或者是实现了特殊方法 reversed 的对象
for length, group in itertools.groupby(reversed(animals), len):
    print(length, "->", list(group))

print("tee" + "==" * 10)

# tee(it, n=2), 产出 n 个独立的迭代器， 每个迭代器都产出相同的项， 就像复制了 it 一样
print(list(itertools.tee('ABC')))

g1, g2 = itertools.tee('ABC')
print(next(g1))
print(next(g2))
print(next(g2))
print(list(g1))

print(list(zip(*itertools.tee('ABC'))))









