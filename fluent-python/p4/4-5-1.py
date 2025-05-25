""" 
处理编码/解码问题

UnicodeEncodeError: 

多数非 UTF 编码解码器只能处理 Unicode 字符的一小部分子集。把
文本转换成字节序列时，如果目标编码没有定义某个字符，则会抛出
UnicodeEncodeError, 除非把 errors 参数传给编码方法或函
数，做特殊处理。
"""

city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859-1'))

# 未能处理的字符 ã 进行编码
# city.encode('cp437')

# 使用 errors 参数
print(city.encode('cp437', errors='ignore')) # 忽略
print(city.encode('cp437', errors='replace')) # 替换为 ? 
print(city.encode('cp437', errors='xmlcharrefreplace')) # 替换为 XML 实体, 这个是不想丢失数据的唯一选择



