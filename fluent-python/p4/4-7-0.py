""" 
Unicode 的规范

unicodedata.normalize 函数

NFC 全称 Normalization Form C， 使用最少的码位构成等价的字符串
NFD 全称 Normalization Form D， 把组合字符分解成基字符和单独的组合字符

通常键盘输入的字符串是 NFC 形式， 但是保存时最好使用 normalize('NFC', user_text) 存储


NFKC 全称 Normalization Form KC， 使用最少的码位构成等价的字符串， 并把组合字符分解成基字符和单独的组合字符
NFKD 全称 Normalization Form KD， 把组合字符分解成基字符和单独的组合字符

"""
from unicodedata import normalize, name

# Unicode 视为相等的两个字符， Python 看到是不同的码点序列，因此判断两者不等
s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'

print(s1, s2)
print(s1 == s2)

# 使用unicodedata.normalize 函数， 使用 Unicode 标准名称来规范化字符串
print(normalize('NFC', s1), normalize('NFC', s2))
print(normalize('NFD', s1), normalize('NFD', s2))

print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))


print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

print("--------------------------------")

# 使用 NFC 时，有些单体字符会被规范化成另一个单体字符
ohm = '\u2126'
print(name(ohm)) # OHM SIGN

ohm_c = normalize('NFC', ohm)
print(name(ohm_c)) # GREEK CAPITAL LETTER OMEGA

print(ohm == ohm_c) # False 

print(normalize('NFC', ohm) == normalize('NFC', ohm_c)) # True


print("--------------------------------")

half = '\N{VULGAR FRACTION ONE HALF}'
print(half)
print(normalize('NFKC', half))

for char in normalize('NFKC', half):
    print(char, name(char), sep='\t')


print("--------------------------------")

four_squared = '4²'
print(four_squared)
print(normalize('NFKC', four_squared))

for char in normalize('NFKC', four_squared):
    print(char, name(char), sep='\t')

print("--------------------------------")


micro = 'μ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(micro == micro_kc)

print(ord(micro), ord(micro_kc), sep='\t')
print(name(micro), name(micro_kc), sep='\t')










