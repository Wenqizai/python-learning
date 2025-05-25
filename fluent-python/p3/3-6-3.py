""" 
dict 的变体

collections.Counter: 对 key 计数的映射， 更新 key 时，会自动计数
"""

import collections

ct = collections.Counter('abracadabra')
print(ct)

ct.update('aaaaazzz')
print(ct)

# 获取出现次数最多的元素的前 3 个（注意， 这里 b 和 r 是并列的， 但是这个方法只会显示前 3 个）
print(ct.most_common(3))

