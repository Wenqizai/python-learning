""" 
BOM：有用的乱码
"""

u16 = 'El Niño'.encode('utf-16')

# 开头的 b'\xff\xfe 是 BOM，表示 UTF-16 编码
print(u16) # b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'


print(list(u16)) # [255, 254, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]


# UTF-16LE 小端编码
u16le = 'El Niño'.encode('utf-16le')
print(list(u16le)) # [69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]

# UTF-16BE 大端编码
u16be = 'El Niño'.encode('utf-16be')
print(list(u16be)) # [0, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111]

