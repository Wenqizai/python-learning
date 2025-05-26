""" 
字符数值的意义
"""

import unicodedata
import re

re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

# 例子说明 re_dig(正则) 和 isdig 匹配的数值并不全面，
# isnumeric 匹配的数值更全面
for char in sample:
    print(f'U+{ord(char):04x}',
            char.center(6),
            're_dig' if re_digit.match(char) else '-',
            'isdig' if char.isdigit() else '-',
            'isnum' if char.isnumeric() else '-',
            f'{unicodedata.numeric(char):5.2f}',
            unicodedata.name(char),
            sep='\t'
          )


