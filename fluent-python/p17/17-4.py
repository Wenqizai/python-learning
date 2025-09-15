""" 
可迭代对象和迭代器：

实现 __iter__ 方法的对象是可迭代对象, __iter__ 方法返回一个迭代器
实现 __getitem__ 方法的对象是序列, 接受从 0 开始的索引， 这种对象也是可迭代的
"""
from sentence import Sentence

s = 'ABC'
for char in s:
    print(char)

print("=" * 10)

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration: # 遇到 StopIteration 异常时， 迭代器耗尽
        del it # 释放对 it 的引用，废弃迭代器对象
        break

s2 = Sentence('Life is short')
it = iter(s2)

print(it)
print(next(it)) # Life, next(it) 相当于 pop
print(next(it)) # is
print(next(it)) # short
# print(next(it)) # StopIteration

print(list(it)) # [] 迭代器已经耗尽, 返回空数组
print(list(iter(s2))) # 重新构建数据迭代器