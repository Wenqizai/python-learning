""" 
使用 * 来拆包
"""
def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


# 在函数调用中多次使用 * 
print(fun(*[1, 2], 3, *range(4, 7)))


print("--------------------------------")

# 元组
t = *range(4), 4
print(t)
# 列表
print([*range(4),  4])
# 集合
print({*range(4), 4, *(5, 6, 7)})


