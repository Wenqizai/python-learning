""" 
unicode 数据库：根据名称查找字符

unicode 数据库记录了字符是否可以打印，是不是字母，是不是数字，是不是标点符号，是不是其他数值符号

如 str.isalpha(), str.isdigit(), str.isspace(), str.isupper(), str.islower(), str.istitle() 就是根据 unicode 数据库中的信息来判断的
"""

from unicodedata import name

print(name('A'))
print(name('é'))

print(name('😅'))
print(name('😭'))









