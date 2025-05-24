""" 
Numpy 是一个非常强大的科学计算库，提供了多维数组对象（ndarray）和各种派生对象（如掩码数组和矩阵）

Numpy 的数组与 Python 标准库中的列表不同，列表存储的是对象的引用，而 Numpy 数组存储的是值

Numpy 数组比 Python 列表更紧凑，更小，更灵活

NumPy 和 SciPy 这两个库中的函数大多是用 C 或 C++ 实现的，可以利用所有 CPU 核
"""
import numpy as np
from time import perf_counter as pc
from random import random
from array import array

a = np.arange(12)
print(a)

print("--------------------------------")

# 查看数组类型
print(type(a))

print("--------------------------------")

# 查看数组形状
print(a.shape)
a.shape = 3, 4 # 3 行 4 列
print(a)

print(a[2]) # 查看第 3 行
print(a[2, 1]) # 查看第 3 行第 2 列

print(a[:, 1]) # 查看第 2 列

print("--------------------------------")

print(a.transpose()) # 转置

print("--------------------------------")

# 查看数组维度
print(a.ndim)

print("--------------------------------")

# 查看数组元素个数
print(a.size)

# NumPy 的高级操作
print("------------- NumPy 的高级操作 -------------------")

# 从文本文件中加载 1000 万个浮点数
# 把 floats 数组中每个元素都乘以 .5
# 把 floats 数组中每个元素都除以 3，并计算耗时

# 写入 1000 万个浮点数到文件 floats-10M-lines.txt
# floats = array('d', (random() for i in range(10**7)))
# open('floats-10M-lines.txt', 'w').write('\n'.join(str(f) for f in floats))

floats = np.loadtxt('floats-10M-lines.txt')

# 查看最后 3 行
print(floats[-3:])

floats *= .5
print(floats[-3:])

# 使用 NumPy 计算均值
t0 = pc(); floats /= 3; print(pc() - t0)

np.save('floats-10M.npy', floats)

t1 = pc();
floats2 = np.load('floats-10M.npy', 'r+')
floats2 *= 6
print(floats2[-3:])
print(pc() - t1)


