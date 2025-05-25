""" 
系统环境检查
"""

import sys
from unicodedata import name

print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdout.encoding:', sys.stdout.encoding)
print()

test_chars = [
    '\N{HORIZONTAL ELLIPSIS}', # cp1252中存在，cp437中不存在
    '\N{INFINITY}', # cp437中存在，cp1252中不存在
    '\N{CIRCLED NUMBER FORTY TWO}', # cp437和cp1252中都不存在
]

for char in test_chars:
    print(f'Trying to output {name(char)}:')
    print(char)