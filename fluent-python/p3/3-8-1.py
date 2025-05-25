""" 
字典视图

dict 的实例方法 .keys(), .values(), .items(), 返回是字典的视图
"""

# .values()
d = dict(a=10, b=20, c=30)
values = d.values()
print(values)

print(len(values))

print(list(values))

print(reversed(values))

# 不能使用 [] 访问视图的元素
# print(values[0])
# values[0] = 'x'

# 视图的元素是原字典的值的引用， 所以可以修改原字典的值
d['z'] = 40
print(d)
print(values)


