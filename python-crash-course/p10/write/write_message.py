""" 
    写入文件, python 只能写入字符串类型到文件中，如果是数值类型，需要先转换为字符串类型
    
"""
from pathlib import Path

# 如果文件不存在，先构建文件
path = Path('resources/programming.txt')
if not path.exists():
    path.touch()


# write_text() 方法每次写入都是第一行，存在覆盖问题
path.write_text('I love programming in Python.')

# 写入数字，先转换为字符串
path.write_text(str(53343))


# 写入多行
contents = 'I love programming in Python.\n'
contents += 'I love programming in Java.\n'
contents += 'I love programming in C++.\n'
path.write_text(contents)

