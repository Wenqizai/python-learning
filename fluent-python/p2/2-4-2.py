""" 
    元组存储的是应用，元祖类指针不可更改，但指针指向的对象是可变的，相当于变相改变元组的数据
    相同大小的元组对象列表，性能和内存占用上更优，python 有专门做了优化
"""

a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(a == b) # True
print(a is b) # False

b[-1].append(99) # 最后一位列表对象，指向的内存地址不变，列表对象内容改变
print(a == b) # False
print(b) # (10, 'alpha', [1, 2, 99])

# 判断一个元组是否固定
tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])

def fixed(obj_name):
    try:
        hash(obj_name)
        return True
    except TypeError:
        return False

print(fixed(tf)) # True
print(fixed(tm)) # False



