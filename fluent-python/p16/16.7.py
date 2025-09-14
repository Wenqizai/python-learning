""" 
Python 中的算术运算符
"""

import numpy as np

# 加法/拼接： +，__add__, __radd__, __iadd__
print(f'+: 1 + 2 = {1 + 2}') # 3

# 减法： -，__sub__, __rsub__, __isub__
print(f'-: 1 - 2 = {1 - 2}') # -1

# 乘法/复制： *，__mul__, __rmul__, __imul__
print(f'*: 1 * 2 = {1 * 2}') # 2
print(f'*: "*" * 2 = {"*" * 2}') # **

# 除法： /，__truediv__, __rtruediv__, __itruediv__
print(f'/: 1 / 2 = {1 / 2}') # 0.5

# 整除：//，__floordiv__, __rfloordiv__, __ifloordiv__
print(f'//: 1 // 2 = {1 // 2}') # 0

# 取模：%，__mod__, __rmod__, __imod__
print(f'%: 1 % 2 = {1 % 2}') # 1

# 返回由商和余数构成的元组：divmod(), __divmod__, __rdivmod__, __idivmod__
print(f'divmod(): divmod(1, 2) = {divmod(1, 2)}') # (0, 1)

# 求幂：**，__pow__, __rpow__, __ipow__
print(f'**: 2 ** 2 = {2 ** 2}') # 4

# 矩阵乘法：@，__matmul__, __rmatmul__, __imatmul__
# 使用 numpy 数组支持 @ 运算符
v1 = np.array([1, 2])
v2 = np.array([3, 4])
print(f'@ (向量点积): [1,2] @ [3,4] = {v1 @ v2}') # 11 = 1 * 3 + 2 * 4

# 矩阵乘法示例
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(f'@ (矩阵乘法): A @ B = \n{A @ B}') # 

print(f'位运算：{"=" * 5}')

# 位与： &，__and__, __rand__, __iand__
print(f'&: 1 & 2 = {1 & 2}') # 0

# 位或： |，__or__, __ror__, __ior__
print(f'|: 1 | 2 = {1 | 2}') # 3

# 位异或： ^，__xor__, __rxor__, __ixor__
print(f'^: 1 ^ 2 = {1 ^ 2}') # 3

# 位取反： ~，__invert__, __rinvert__, __iinvert__
print(f'~: ~1 = {~1}') # -2

# 位左移： <<，__lshift__, __rlshift__, __ilshift__
print(f'<<: 1 << 2 = {1 << 2}') # 4

# 位右移： >>，__rshift__, __rrshift__, __irshift__
print(f'>>: 1 >> 2 = {1 >> 2}') # 0

# 位补全： <<, __lshift__, __rlshift__, __ilshift__