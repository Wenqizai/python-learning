""" 
dict 视图的集合运算
"""

d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50, f=60)

# dict_keys 和 dict_items 实现了一些特殊方法，支持集合的运算符
print(d1.keys() & d2.keys())
print(d1.keys() | d2.keys())
print(d1.keys() - d2.keys())


# 字典的视图亦可以与 set 进行运算
s = {'a', 'e', 'i'}
print(s & d1.keys())

print(s | d1.keys())