""" 
运行时可检查的静态协议
"""
from typing import SupportsComplex
import numpy as np
import numbers

c64 = np.complex64(3 + 4j)
print(isinstance(c64, complex))
print(isinstance(c64, SupportsComplex))

c = complex(c64)
print(c)

print(isinstance(c, complex))
print(isinstance(c, SupportsComplex))

print(complex(c))

# 测试对象 c64 是不是 complex 或 SupportsComplex, 可以构造层元组
print(isinstance(c64, (complex, SupportsComplex)))
# 或者检查父类, complex64, complex128 都是 numbers.Complex 的虚拟子类
print(isinstance(c64, numbers.Complex))

# 不是使用鸭子类型时, 做判断
o = complex(c64)
if isinstance(o, (complex, SupportsComplex)):
    # o 可以转换成复数时, 执行的一些操作
    ...
else:
    raise TypeError('o must be convertible to complex')

if isinstance(o, numbers.Complex):
    # o 是 Complex 实例时执行一些操作
    ...
else:
    raise TypeError('o must be an instance of Complex')

# 使用鸭子类型时, 做判断
try:
    c = complex(o)
except TypeError as exc:
    raise TypeError('0 must be convertible to complex') from exc