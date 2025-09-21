""" 
可迭代的归约函数
"""

print("## all", "===" * 10)

# all(it), it 中的所有项都为真值时返回 True，否则返回False；all([]) 返回 True
print(all([1, 2, 3]))

print(all([1, 0, 3]))

print(all([]))


print('## any', '===' * 10)

# any(it), it 中的任一项为真值时返回 True，否则返回False；any([]) 返回 False
print(any([1, 2, 3]))
print(any([1, 0, 3]))
print(any([0, 0, 0]))
print(any([]))

g = (n for n in [0, 0.0, 7, 8])
print(any(g)) # 迭代到第一个 True
print(next(g))

