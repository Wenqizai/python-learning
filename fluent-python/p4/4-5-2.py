""" 
处理编码/解码问题

UnicodeDecodeError: 

从二进制序列转换成文本时，如果指定了编码方式 utf-8等，无法转换时，会抛出 UnicodeDecodeError

其中 'cp1252', 'iso8859_i', 'koi8_r' 等陈旧的 8 位编码能解码任何字节序列，而不会抛出错误，呈现是乱码
"""

octets = b'Montr\xe9\xael'
print(octets.decode('cp1252'))
print(octets.decode('iso8859-1'))
print(octets.decode('koi8_r'))

# 无法解码，抛出 UnicodeDecodeError
# print(octets.decode('utf-8'))

# 使用 errors 参数
print(octets.decode('utf-8', errors='replace')) # 替换为 �



