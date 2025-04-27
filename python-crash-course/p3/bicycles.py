bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

print(bicycles[0].upper())
print(bicycles[0].title())
print(f"My first bicycle was a {bicycles[0].title()}")


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# 在指定 index 位置中插入元素
motorcycles.insert(0, 'honda')
print(motorcycles)

# 删除指定 index 的元素, 没有返回值
del motorcycles[0]
print(motorcycles)

# 删除指定值的元素（删除第一个匹配的元素）
motorcycles.remove('ducati')
print(motorcycles)

# 移除列表中最后一个元素
motorcycles.pop()
print(motorcycles)

# 移除列表中指定 index 的元素，带返回值
motorcycles.pop(1)
print(motorcycles)