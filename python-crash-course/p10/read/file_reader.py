""" 
    文件读取, resources/pi_digits.txt
"""
from pathlib import Path

# path = Path('pi_digits.txt') # 读当前目录文件可直接读取
path = Path(__file__).parent / 'resources' / 'pi_digits.txt' # 读取其他目录文件需要指定绝对路径
contents = path.read_text()
print(contents)

# 方法 2: 相对路径
path = Path('resources/pi_digits.txt')
contents = path.read_text()
print(contents)


# 读取相同目录下的文件, 可以不指定路径
path = Path('_test_file')
contents = path.read_text().strip()
print(contents)

# 删除字符串中的空格
str = "1 w 2".replace(" ", "")
print(str)


# 按行读取
path = Path('resources/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines() # 按行读取
print(lines)

# 按行读取, 并去除空格
lines = [line.strip() for line in lines]
print(lines)

# 按行读取, 并去除空格, 并打印行号
for i, line in enumerate(lines):
    print(f"{i+1}: {line}")



