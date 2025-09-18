""" 
标准库中的生成函数: 把输入的各项扩充成多个输出项的生成器函数
"""
import itertools
import operator

print("count" + "==" * 10)

# count(start=0, step=1), 从 start 开始，按照步长 step 不断产生值
ct = itertools.count()
print(next(ct))
print(next(ct))
print(next(ct), next(ct), next(ct))
print(list(itertools.islice(itertools.count(1, 0.5), 3)))

print("cycle" + "==" * 10)

# cycle(it), 无限循环 it 中的元素
cy = itertools.cycle('ABC')
print(next(cy))
print(list(itertools.islice(cy, 7)))

print("pairwise" + "==" * 10)

# pairwise(it), 返回输入的可迭代对象中 连续 的 重叠对 
print(list(itertools.pairwise(range(7))))


print("repeat" + "==" * 10)

# repeat(item, [times]), 重复不断地产出指定的项，除非 times 指定次数, 到达指定次数后抛异常：StopIteration
rp = itertools.repeat(7)
print(next(rp), next(rp))

print(list(itertools.repeat(8, 4)))

print(list(map(operator.mul, range(11), itertools.repeat(5))))

print("combinations" + "==" * 10)

# combinations(it, outlen), 把 it 产出的 outlen 个项组合在一起，然后产出
print(list(itertools.combinations('ABC', 2)))

print("combinations_with_replacement" + "==" * 10)

# 把 it 产出的 outlen 个项组合在一起，然后产出，包含重复项的组合
print(list(itertools.combinations_with_replacement('ABC', 2)))

print("permutations" + "==" * 10)

# permutations(it, outlen), 把 it 产出的 outlen 个项排列在一起，然后产出
print(list(itertools.permutations('ABC', 2)))

print("product" + "==" * 10)

# product(it1, ..., itN), 计算笛卡尔积，返回元组数组，相当于多重循环的效果
print(list(itertools.product('ABC', repeat=2)))