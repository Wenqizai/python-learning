""" 
unicode 的规范化：规范化文本匹配的实用函数

1. NFC 是最好的规范化比较 str
2. 不区分大小写比较使用 str.casefold()
3. 处理多语言文本 nfc_equal 和 fold_equal 函数
"""
from unicodedata import normalize

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold()



# 1. 使用 NFC 规范化, 区分大小写
s1 = 'café'
s2 = 'cafe\u0301'

print(s1, s2)
print(s1 == s2)
print(nfc_equal(s1, s2))
print(nfc_equal('A', 'a'))

print("--------------------------------")

# 2. 不区分大小写比较使用 str.casefold()

s3 = 'Straße'
s4 = 'strasse'

print(s3 == s4)
print(nfc_equal(s3, s4))
print(fold_equal(s3, s4))
print(fold_equal('A', 'a'))
print(fold_equal(s1, s2))

print("--------------------------------")







