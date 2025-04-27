cars = ['bmw', 'subaru', 'audi', 'toyota']
cars.sort()
print(cars)

# 倒序
cars.sort(reverse=True)
print(cars)

# 临时排序，不改变原有 list 顺序
print("Here is the original list:" + str(cars))
print("Here is the sorted list:" + str(sorted(cars)))
print("Here is the reverse sorted list:" + str(sorted(cars, reverse=True)))
print("Here is the original list again:" + str(cars))

# 反转列表，不是排序
cars = ['bmw', 'subaru', 'audi', 'toyota']
cars.reverse()
print(cars)

# 列表长度
print(len(cars))