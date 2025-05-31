""" 
垃圾回收: CPython 使用引用计数进行垃圾回收

CPython 2.0 增加分代垃圾回收, 检查循环引用
"""
import weakref

s1 = {1, 2, 3}
s2 = s1

def bye():
    print("Gone with the wind...")

ender = weakref.finalize(s1, bye) # 注册回调函数, 当 s1 被删除时调用
print(ender.alive)

del s1 
print(ender.alive) # del s1 此时对象还没被删除, 因为 s2 还在引用

s2 = 'spam'
print(ender.alive) # s2 被重新赋值, s1 被删除, 对象被删除, 回调函数被调用
