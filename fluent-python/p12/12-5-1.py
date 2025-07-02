""" 
切片原理
"""
class MySeq:
    def __getitem__(self, index):
        return index

s = MySeq()
print(s[1]) # 直接返回索引
print(s[1:4]) # 返回切片，1开始，4结束
print(s[1:4:2]) # 返回切片，1开始，4结束，2步长

print(s[1:4:2, 9]) # [] 中间有逗号, 识别出为元组 (slice(1, 4, 2), 9)
print(s[1:4:2, 7:9]) # (slice(1, 4, 2), slice(7, 9, None))

print(s[1:4:2, 7:9, 5]) # (slice(1, 4, 2), slice(7, 9, None), 5)
print(s[1:4:2, 7:9, 5, 1:3]) # (slice(1, 4, 2), slice(7, 9, None), 5, slice(1, 3, None))

print("-"*50)
print(slice)
print(dir(slice))

print("-"*50)

print(slice(None, 10, 2).indices(5)) # 长度为 5 的切片, 相当于 (0, 5, 2)
print(slice(-3, None, None).indices(5)) # 长度为 5 的切片, 相当于 (2, 5, 1)