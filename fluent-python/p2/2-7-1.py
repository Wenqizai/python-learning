""" 
    切片
    所有的序列类型都支持切片操作，如 list, str, tuple

    切片操作符的语法是 start:stop:step
    step 为负数时，表示反向

    slice.indices(len(l) 可以帮助计算返回 (actual_start, actual_stop, actual_step)，方便规范用户随意设置的切片参数
"""

l = [10, 20, 30, 40, 50, 60]

# 从开始到下标2（不包括下标2）  
print(l[:2]) # 输出 [10, 20]

# 从下标2开始到结束
print(l[2:]) # 输出 [30, 40, 50, 60]

# 从开始到下标3，步长为2
print(l[:3:2]) # 输出 [10, 30]

# 从开始到结束，步长为2
print(l[::2]) # 输出 [10, 30, 50]

# 切片操作符还可以用于字符串和元组
s = "Hello, World!"
print(s[:5]) # 输出 "Hello"
print(s[7:12]) # 输出 "World"

# 步长可以是负数, 表示反向
s = 'bicycle'
print(s[::3]) # 输出 "bye"
print(s[::-1]) # 输出 "elcycib"，从后往前，步长为1
print(s[::-2]) # 输出 "eccb"，从后往前，步长为2

# 切片操作符还可以用于列表的嵌套
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

slice = slice(1, 5, 2)  # 切片对象
print(l[slice])  # 等价于 l[1:3:2]

# 使用slice对象的indices方法，可以计算出切片后的索引范围
print(slice.indices(len(l))) # 输出 (1, 3, 2)


