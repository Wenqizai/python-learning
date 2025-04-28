cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 检查是否相等, 区分大小写
print(car == 'toyota')
print(car == 'Toyota')

# 检查是否不相等
print(car != 'toyota')
print(car != 'Toyota')


# 比较数字
print(1 == 1)
print(1 == 2)

# 检查多个条件
print(1 < 2 and 2 < 3)
print(1 < 2 and 2 > 3)