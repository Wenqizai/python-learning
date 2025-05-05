""" 
    文件逐行读取, resources/pi_digits.txt
"""
from pathlib import Path

# 一次性读取，逐行打印
path = Path('resources/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)
    
    
print("-" * 100) # 打印 100 个 -，字符串可以乘以一个整数，代表重复，但是不能乘以浮点数

# 逐行读取，逐行打印
path = Path('resources/pi_digits.txt')
with path.open(mode='r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())