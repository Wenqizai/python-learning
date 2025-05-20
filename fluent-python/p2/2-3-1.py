symbols = '$¢£¥€¤'

# append
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# 列表推导
codes = [ord(symbol) for symbol in symbols]
print(codes)

# 使用生成器表达式
codes = list(ord(symbol) for symbol in symbols)
print(codes)

# 多行列表示例
fruits = [
    'apple',
    'banana',
    'orange',
    'grape',  # 末尾逗号
]

# 多行字典示例
person = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'country': 'USA',  # 末尾逗号
}

# 多行元组示例
coordinates = (
    10,
    20,
    30,  # 末尾逗号
)

# 多行列表推导式示例
squares = [
    x * x
    for x in range(10)
    if x % 2 == 0
]

# 错误示例：续行符后多了一个空格
# 这行会报错
# result = 1 + \
#  2

# 正确的续行方式
result = 1 + \
    2

print(fruits)
print(person)
print(coordinates)
print(squares)
print(result)

x = 'ABC'
codes = [ord(x) for x in x]
print(codes)

# 使用生成器表达式
codes = [last := ord(c) for c in x]
print(codes)
print(last)
# print(c) # c 未定义

