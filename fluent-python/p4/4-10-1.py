""" 
支持 str 和 bytes 的双模式 API: 正则

str 的正则匹配比 bytes 更加丰富
"""

import re

re_numbers_str = re.compile(r'\d+') # numbers 能匹配泰米尔数字和 ascii 数字
re_numbers_bytes = re.compile(rb'\d+') # numbers 只能能匹配 ascii 数字

re_words_str = re.compile(r'\w+') # words 能匹配字母， 上标， 泰米尔数字和 ascii 数字
re_words_bytes = re.compile(rb'\w+') # words 只能匹配 ascii 字母， 数字和下划线

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            "as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode('utf-8')

print(f'Text \n {text_str!r}')
print('Numbers')

print(' str  : ', re_numbers_str.findall(text_str))
print(' bytes: ', re_numbers_bytes.findall(text_bytes))

print('Words')

print(' str: ', re_words_str.findall(text_str))
print(' bytes: ', re_words_bytes.findall(text_bytes))

