""" 
不可变映射, MappingProxy, 是只读的， 不能修改， 但是可以修改原映射, 相当于可以修改 d，不能修改 d_proxy
"""

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)

print(d_proxy)

print(d_proxy[1])

# d_proxy[2] = 'x' # TypeError: 'mappingproxy' object does not support item assignment

d[2] = 'B'
print(d_proxy)
print(d_proxy[2])


