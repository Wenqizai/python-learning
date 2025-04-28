players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3]) # 0 -> 3
print(players[1:4]) # 1 -> 4
print(players[:3]) # 0 -> 3
print(players[2:]) # 2 -> 

print(players[-3:]) # 从倒数第三个开始到结束
print(players[-1:]) # 从倒数第一个开始到结束
print(players[:-1]) # 从开始到倒数第二个 （不包含倒数第一个）
print(players[:-2]) # 从开始到倒数第三个 （不包含倒数第二个）


print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(f'{player.title()}\n')






