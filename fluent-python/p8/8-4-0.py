""" 
类型由受支持的操作定义
"""
import abc

# 这里的 x 可以是 int, complex, Fraction, numpy.uint32 等数字类型
# 也可以是 str, tuple, list, dict, set, bytes, bytearray 等序列类型
def double(x):
    return x * 2

# 参数类型是 Sequence 的子类，可用工具静态检查
def double(x: abc.Sequence):
    return x * 2

