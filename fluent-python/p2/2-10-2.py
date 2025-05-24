""" 
memoryview 是一种共享内存的序列类型，可以不复制内容的情况下处理原数组的切片
因为不涉及内存复制，所以 memoryview 很高效

memoryview 可以与任何可迭代对象或可变序列对象创建，只要该对象支持缓冲协议（即该对象有 __buffer__ 或 __array__ 方法）

"""
from array import array

octets = array('B', range(6))

print(octets)

m1 = memoryview(octets)
print(m1.tolist())

# 将 octets 转换为 2 行 3 列的数组
m2 = m1.cast('B', [2, 3])
print(m2.tolist())

# 将 octets 转换为 3 行 2 列的数组
m3 = m1.cast('B', [3, 2])
print(m3.tolist())

# 修改 m2 和 m3 的值，会直接影响到 octets 的值
m2[1, 1] = 22
m3[1, 1] = 33

print(octets)


# 修改一个 16 位整数数组的某一项直接，改变该项的值
numbers = array('h', [-2, -1, 0, 1, 2])

memv = memoryview(numbers)
print(len(memv))

print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(memv_oct.tolist())

print(numbers)



