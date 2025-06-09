""" 
注解中可用的类型: 泛化容器

Python 容器是异构的, 在一个 list 可以混合存放不同类型

泛化容器: 
list[T] 表示一个列表, 列表中的元素类型为 T
dict[K, V] 表示一个字典, 字典的键类型为 K, 值类型为 V
tuple[T1, T2, ...] 表示一个元组, 元组中的元素类型为 T1, T2, ...

"""

# 返回值类型为 list[str], 表示列表中的元素类型为 str
def tokenize(text: str) -> list[str]:
    return text.upper().split()

