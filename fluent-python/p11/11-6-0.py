""" 
格式化展示
"""
import Vector2d as Vector2d

br1 = 1 / 4.82
print(br1)

print(format(br1, '0.4f'))

print('1 BRL = {rate:0.2f} USD'.format(rate=br1))

print(f'1 BRL = {br1:0.2f} USD')

# 转二进制
print(format(42, 'b'))
# 转十六进制
print(format(42, 'x'))

# % 百分数形式
print(format(2 / 3, '.1%'))

v1 = Vector2d.Vector2d(3, 4)
print(format(v1))
print(format(v1, '.3f'))
print(format(v1, '.3e'))

print("-" * 50)
# 坐标
print(format(Vector2d.Vector2d(1, 1), 'p'))
print(format(Vector2d.Vector2d(1, 1), '.3ep'))
print(format(Vector2d.Vector2d(1, 1), '.5fp'))