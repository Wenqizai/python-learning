""" 
使用 iter 处理可调用对象
"""
import random

def d6():
    return random.randint(1, 6)

d6_iter = iter(d6, 1) # 1 是哨兵值，当 d6() 返回值等于 1 时就会停止
print(d6_iter)

for roll in d6_iter:
    print(roll)