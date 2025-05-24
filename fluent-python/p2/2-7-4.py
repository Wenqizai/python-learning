"""  
    为切片赋值
"""

l = list(range(10))

print(l)

# 为切片赋值, 2-5 被替换为 [20, 30]
l[2:5] = [20, 30]
print(l)

# 删除指定切片
del l[5:7]
print(l)

# 为切片赋值, 将 11, 22 赋值给索引为 3 和 5 的元素
l[3::2] = [11, 22]
print(l)

# 只能赋值可迭代对象
# l[2:5] = 100 # 报错：TypeError: must assign iterable to extended slice
# print(l)

l[2:5] = [100]
print(l)

# (100) 不是元组，而是整数 100， （100,） 是包含一个整数的元组
l[2:3] = (100,)
print(l)


