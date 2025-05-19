import math
from vector2d import Vector

v1 = Vector(1, 2)
v2 = Vector(3, 4)

# 演示 __str__ 和 __repr__ 的区别
print("使用 str():", str(v1))      # Vector(1, 2)
print("使用 repr():", repr(v1))    # Vector(x=1, y=2)
print("直接打印:", v1)             # Vector(1, 2)
print("交互式环境显示:", v1)       # Vector(x=1, y=2)

# 原始测试
print(v1 + v2)  # Vector(4, 6)
print(v1 * 3)   # Vector(3, 6)
print(abs(v1))  # 2.23606797749979

# 测试 __repr__
v1 = Vector(1, 2)
v2 = Vector(0, 0)
print(f"repr输出: {repr(v1)}")     # 显示详细信息，包含参数名
print(f"在调试器中: {v1!r}")      # !r 强制使用 __repr__

# 测试 __bool__
print(f"v1是否为真: {bool(v1)}")  # True，因为向量长度不为0
print(f"v2是否为真: {bool(v2)}")  # False，因为向量长度为0

# 在条件语句中使用
if v1:
    print("v1是非零向量")
if not v2:
    print("v2是零向量")

# 1. 格式说明符示例
print("\n=== 格式说明符示例 ===")
print(f"默认格式化 {v1}")      # 使用 __str__
print(f"使用!s: {v1!s}")       # 显式使用 __str__
print(f"使用!r: {v1!r}")       # 显式使用 __repr__
print(f"使用!a: {v1!a}")       # 使用 ascii() 函数

# 2. bool()函数用法示例
print("\n=== bool()函数用法示例 ===")
# 直接使用bool()
print(f"bool(v1) = {bool(v1)}")    # True (非零向量)
print(f"bool(v2) = {bool(v2)}")    # False (零向量)

# 在条件语句中隐式使用bool
if v1:
    print("v1是非零向量")
if not v2:
    print("v2是零向量")

# 其他类型的bool示例
print("\n=== 其他类型的bool示例 ===")
print(f"bool('') = {bool('')}")           # False (空字符串)
print(f"bool('hello') = {bool('hello')}") # True (非空字符串)
print(f"bool([]) = {bool([])}")           # False (空列表)
print(f"bool([1,2]) = {bool([1,2])}")    # True (非空列表)
print(f"bool(0) = {bool(0)}")            # False
print(f"bool(1) = {bool(1)}")            # True
print(f"bool(None) = {bool(None)}")      # False
