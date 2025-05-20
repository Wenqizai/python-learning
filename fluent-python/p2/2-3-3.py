colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# 等价于
tshirts = []
for color in colors:
    for size in sizes:
        tshirts.append((color, size))
print(tshirts)


# 生成器表达式
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)
