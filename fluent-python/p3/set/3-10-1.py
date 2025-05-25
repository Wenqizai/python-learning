""" 
集合 Set : 集合的元素必须是可散列的， 不可变， 且具有唯一性

集合的运算符

a | b : 并集
a & b : 交集
a - b : 差集
a ^ b : 对称差集

创建 set 需要使用 set(), 不能使用 {} 创建， {} 创建的是 dict
"""

s1 = {'spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs'}
print(s1) # 无序

# 如果要保留顺序
k1 = dict.fromkeys(s1).keys()
s2 = list(k1)
print(k1) # 保留顺序
print(s2)


s2 = set('hello')
print(s2)



set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)


s = {1}
print(type(s))
print(s )
print(s.pop())
print(s)

# frozenset 需要构造函数创建
print(frozenset(range(10)))