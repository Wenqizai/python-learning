""" 
映射类型的标准 API

可 hash
"""

from collections import abc

my_dict = {}

print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))

tt = (1, 2, (30, 40))
print(hash(tt))

t1 = (1, 2, [30, 40])
# print(hash(t1))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))












