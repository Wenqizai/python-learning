""" 
set 推导式
"""
# 从 unicodedata 模块中获取所有字符的名称
from unicodedata import name

# 将代码在 32 - 255 范围内，而且名称带有 ‘SIGN’ 的代码打印出来
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})



