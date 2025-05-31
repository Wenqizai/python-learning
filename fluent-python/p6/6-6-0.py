""" 
del 和垃圾回收

del 是删除引用数据, 不是删除对象数据, 对象不可达时会被垃圾回收

__del__ 方法, 对象被删除时调用, 这时可以用来释放外部的资源
"""

a = [1, 2, 3]
b = a

del a
print(b) # a 的引用被删除, 但是对象数据还在, 所以 b 还是能访问到对象数据
print(a) # NameError: name 'a' is not defined