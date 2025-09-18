""" 
标准库中的生成函数：用于筛选的生成器函数
"""
import itertools

def vowel(c):
    return c.lower() in 'aeiou'

# filter(predicate, it), 过滤序列中的元素， predicate 为 True 的元素会被保留
print(list(filter(vowel, 'Aardvark')))
print(list(itertools.filterfalse(vowel, 'Aardvark')))

print("==" * 10)

# dropwhile(predicate, it), 跳过序列中 predicate == True 的元素，但只会跳过一次
print(list(itertools.dropwhile(vowel, 'Aardvark')))

# takewhile(predicate, it), 一直取 predicate == True 的元素，直到取到返回 False 后停止
print(list(itertools.takewhile(vowel, 'Aardvark')))

print("==" * 10)

# compress(it, selector_it), 根据 selector_it 的元素为 True 或 False，选择 it 中的元素
print(list(itertools.compress('Aardvark', (1,0,1,0,1,1,0,1))))

print("==" * 10)

# islice(it, stop) 或 islice (it, start, stop, step=1)，产生切片
print(list(itertools.islice('Aardvark', 4)))
print(list(itertools.islice('Aardvark', 4, 7)))
print(list(itertools.islice('Aardvark', 1, 7, 2)))

print("==" * 10)
