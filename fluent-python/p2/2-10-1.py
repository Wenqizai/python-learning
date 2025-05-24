""" 
  列表以外的序列类型，数组

  注：Set 是可迭代对象，但不是序列，Set 是无序的


  数组：只允许存储同一种数据类型，相比 list 更紧凑，更节省内存

  Python 3.10 开始，array 没有像 list 那样原地排序，只能使用内置函数 sorted 排序

  对于已经有序的数组，使用 bisect 模块的 insort 函数插入新元素，可以保持数据的有序，无须重新排序
  eg：bisect.insort(my_array, new_item_2)
"""
from array import array
from random import random

# 生成 1000 万个随机数
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

# 将数组存入一个二进制文件
# 写入文件大小， double 占用 8 个字节， 8 * 10**7 = 80000000 字节 = 80MB
fp = open('./floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# 从文件读取到数据中
floats2 = array('d')
fp = open('./floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

print(floats2[-1])
print(floats2 == floats)



