# 元组，不可变的列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (400, 100)
print(dimensions)

# dimensions[0] = 250 # 报错，元组不可变

# 遍历元组
for dimension in dimensions:
    print(dimension)

# 修改元组变量
dimensions = (200, 100)
print(dimensions)
