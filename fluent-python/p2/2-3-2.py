""" 
列表推导式与map和filter的比较
"""
symbols = '$¢£¥€¤'

# 列表推导式
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# 使用map和filter
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# map 用法：对每个元素应用函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(f"map 示例 - 平方: {squared}")  # [1, 4, 9, 16, 25]

# filter 用法：筛选满足条件的元素
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter 示例 - 偶数: {even_numbers}")  # [2, 4]

# 组合使用
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 先筛选偶数，再平方
result = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
print(f"组合示例 - 偶数的平方: {result}")  # [4, 16, 36, 64, 100]

# 实际应用：处理字符串
text = "Hello123World"
# 只保留字母
letters = list(filter(lambda c: c.isalpha(), text))
print(f"只保留字母: {letters}")  # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']

# 转换为大写
upper_letters = list(map(lambda c: c.upper(), letters))
print(f"转换为大写: {upper_letters}")  # ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']
