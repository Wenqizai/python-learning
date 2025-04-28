# 嵌套，列表中嵌套字典，字典 value 嵌套列表

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# 使用 range() 生成多个外星人
aliens = []

i = 0;
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': i, 'speed': 'slow'}
    aliens.append(new_alien)
    i += 1

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print(f"...")

