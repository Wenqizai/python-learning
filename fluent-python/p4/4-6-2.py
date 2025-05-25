""" 
处理文本文件

除非想判断编码，否则不要以二进制模式打开文本文件。即
便你真的想判断编码，也应该使用 Chardet，而不要重新发明轮
子（参见 4.5.4 节）。一般来说，二进制模式只能用于打开二进
制文件，例如光栅图像。
"""

import os

fp = open('cafe.txt', 'w', encoding='utf_8') # 返回指定编码方式的 <_io.TextIOWrapper> 对象
print(fp)

print(fp.write('café')) # write 返回的是 unicode 字符数
fp.close()


print(os.stat('cafe.txt').st_size) # 读取的字节数，5个，其中 é 占 2 个字节

fp2 = open('cafe.txt') # 不指定编码，使用默认编码 utf-8
print(fp2)
print(fp2.encoding)
print(fp2.read())


fp3 = open('cafe.txt', encoding='utf-8')
print(fp3)
print(fp3.read())


fp4 = open('cafe.txt', 'rb') # 以二进制模式读取文件
print(fp4)  # 返回是一个 buffered 对象
print(fp4.read())





