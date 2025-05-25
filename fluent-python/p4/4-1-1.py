""" 
字符：编码与解码
"""

s = 'café'
print(len(s))

# 编码成 bytes 对象
b = s.encode('utf-8')
print(b)
# 其中 e´ 被编码成两个字节
print(len(b))

# 解码成 str 对象
b.decode('utf-8')
print(b)
print(len(b))








