""" 
bytes 和 bytearray
"""
cafe = bytes('café', encoding='utf-8')
print(cafe)

# 获取字节
print(cafe[0])  # 返回整数
print(cafe[:1]) # 返回长度为 1 的 bytes 对象

cafe_arr = bytearray(cafe)
print(cafe_arr)

print(cafe_arr[-1])

print(bytes.fromhex('31 4B CE A9'))



