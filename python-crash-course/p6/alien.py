alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'x_position': 200, 'y_position': 25, 'speed': 'medium'}
print(alien_0)

new_position = f'{alien_0['x_position']} ' + alien_0['speed']
print(new_position)

# 修改键值对
alien_0['x_position'] = new_position
print(alien_0)

# 添加键值对
alien_0['speed'] = 'fast'
print(alien_0)

# 删除键值对
del alien_0['speed']
print(alien_0)


# 空字典
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 修改 key 的值
alien_0 = {'color': 'green', 'points': 5}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")


# 删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
