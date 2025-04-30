pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# 使用 while 循环，删除列表中所有的 'cat'
while 'cat' in pets:
    pets.remove('cat')

print(pets)