""" 
    读取大文件
"""

from pathlib import Path

path = Path('resources/pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    if line:
        pi_string += line.strip()

# 打印前52位
print(f"{pi_string[:52]}...")
print(len(pi_string))
