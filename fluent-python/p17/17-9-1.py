""" 
标准库中的生成函数：用于映射的生成器函数
"""
import itertools
import operator

simple = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

print("accumulate" + "==" * 10)
# accumulate(it, [func]) 累计值，提供 func 时，会使用 func 计算累计值
print(list(itertools.accumulate(simple)))
print(list(itertools.accumulate(simple, min)))
print(list(itertools.accumulate(simple, max)))

print(list(itertools.accumulate(simple, operator.mul))) # 累乘

print("enumerate" + "==" * 10)

# enumerate(iterable,start=0) 产生 （index, item) 形式的二元组， index 从 start 开始计数
print(list(enumerate('albatroz', 1)))

print("map" + "==" * 10)

# map(func, it1,[it2, ..., itN]) 将 it1, it2, ..., itN 的每个元素传入给 func
print(list(map(operator.mul, range(11), range(11))))


print("starmap" + "==" * 10)

# starmap(func, it) 将 it 的每个元素传入给 func
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))

print(list(enumerate(itertools.accumulate(simple), 1))) # 计算 sample 的累加
print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(simple), 1)))) # 计算平均值
print(list(itertools.starmap(lambda a, b: b / a, enumerate(itertools.accumulate(simple), 1)))) # 计算平均值