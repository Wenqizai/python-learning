""" 
返回不含零值或负值的计数器
"""
from typing import Counter


ct = Counter('abracadabra')
print(ct) # 返回字符的数量计数

ct['r'] = -3
ct['d'] = 0
print(ct) # 更新计算器

print(+ct) # 返回不含零值或负值的计数器