""" 
unicode 的规范化：大小写同一化

大小写同一化其实就是把所有文本变成小写，再做些其他转换

str.casefold() 方法会把字符串变成小写，相当于不区分大小写比较
"""
from unicodedata import name

micro = 'μ'
print(name(micro))

micro_cf = micro.casefold()
print(name(micro_cf))

print(micro, micro_cf)

print("--------------------------------")

eszett = 'ß'
print(name(eszett))

eszett_cf = eszett.casefold()
print(eszett, eszett_cf)
