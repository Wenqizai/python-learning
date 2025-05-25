""" 
处理文本文件
"""

open('cafe.txt', 'w', encoding='utf_8').write('café')

# 读取文件, 这里读取时没有指定编码，在不同平台下读取的编码会有乱码
print(open('cafe.txt').read())

print(open('cafe.txt', encoding='utf_8').read())


