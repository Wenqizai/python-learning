squares = []
for value in range(1, 11): # 生成 1-10 的数字
    square = value ** 2
    squares.append(square)

print(squares)


squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)


squares = [value**2 for value in range(1, 11)]
print(squares)
