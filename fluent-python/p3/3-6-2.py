""" 
dict 的变体

collections.ChainMap, 可以连接多个字典，在逻辑上看成一个字典。

如果多个字典的 key 重复，这 get 时优先取第一个连接的 key 的值。
"""

from collections import ChainMap
import builtins

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)

chain = ChainMap(d1, d2)

print(chain)

print(chain['a'])
print(chain.get('c'))

# chainMap 的更新和插入操作只会影响第一个映射
chain['c'] = -1
print(chain)


pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup['abs'])
