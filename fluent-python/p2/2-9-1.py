""" 
 list.sort 与内置函数 sorted

 list.sort 方法会就地排序列表，会修改传入的列表，不会创建新的列表
 sorted 函数会返回一个新的列表，不会修改传入的列表

  默认情况下，Python 按字符代码的字典顺序排序字符串，即 ASCII 码顺序，大写字母排在小写字母前面

"""

fruits = ['grape', 'raspberry', 'apple', 'banana']

print(fruits)
print(sorted(fruits))
print(fruits)

fruits.sort()
print(fruits)


