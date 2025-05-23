# Python 星号（*）拆包操作符用法总结

Python中的星号（`*`）操作符是一个强大的语法特性，用于序列的拆包和打包。**重要说明：`*` 操作符不仅限于元组，可用于任何可迭代对象**（列表、元组、集合、字符串等）。以下是它的主要用法场景：

## 1. 函数调用中的参数拆包

### 1.1 拆包可迭代对象为位置参数

```python
def add(a, b, c):
    return a + b + c

values = [1, 2, 3]  # 列表
result = add(*values)  # 等同于 add(1, 2, 3)
print(result)  # 6

# 同样适用于元组、集合等可迭代对象
tuple_values = (1, 2, 3)  # 元组
add(*tuple_values)  # 等同于 add(1, 2, 3)
```

### 1.2 在函数调用中多次使用拆包

```python
def func(a, b, c, d, e, f):
    return a, b, c, d, e, f

result = func(*[1, 2], 3, *[4, 5, 6])  # 等同于 func(1, 2, 3, 4, 5, 6)
print(result)  # (1, 2, 3, 4, 5, 6)
```

## 2. 函数定义中的参数收集

### 2.1 收集剩余位置参数

```python
def collect_args(first, *rest):
    print(f"First: {first}")
    print(f"Rest: {rest}")  # rest 始终是元组类型

collect_args(1, 2, 3, 4)
# First: 1
# Rest: (2, 3, 4)
```

**注意：** 在函数定义中，`*args` 总是将参数收集为元组，无论传入的是什么类型的可迭代对象。

## 3. 序列构造中的拆包

### 3.1 元组拆包/打包

```python
# 拆包到元组
numbers = [1, 2, 3, 4]
t = *numbers, 5  # 元组打包
print(t)  # (1, 2, 3, 4, 5)
```

### 3.2 列表拆包

```python
original = [1, 2, 3]
expanded = [0, *original, 4]  # 在列表中间拆包
print(expanded)  # [0, 1, 2, 3, 4]

# 合并多个列表
list1 = [1, 2]
list2 = [3, 4]
merged = [*list1, *list2]
print(merged)  # [1, 2, 3, 4]
```

### 3.3 集合拆包

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
combined = {*set1, *set2}  # 自动去重
print(combined)  # {1, 2, 3, 4, 5}

# 混合拆包
mixed = {*range(4), 4, *(5, 6, 7)}
print(mixed)  # {0, 1, 2, 3, 4, 5, 6, 7}
```

### 3.4 字典拆包（使用 ** 操作符）

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## 4. 变量赋值中的拆包

### 4.1 拆包到多个变量

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]  # 注意这里是列表，不是元组
print(last)    # 5

# 同样适用于元组
first, *middle, last = (1, 2, 3, 4, 5)
print(middle)  # [2, 3, 4]  # 结果仍然是列表
```

**注意：** 在变量赋值中，带星号的变量（如 `*middle`）总是接收一个列表，即使被拆包的是元组或其他类型的可迭代对象。这与函数定义中的行为不同。

### 4.2 忽略部分值

```python
first, *_ = [1, 2, 3, 4, 5]  # 只关心第一个值
print(first)  # 1

# 或者
first, *_, last = [1, 2, 3, 4, 5]  # 只关心首尾
print(first, last)  # 1 5
```

## 5. 注意事项

1. 在单一赋值表达式中，只能有一个带星号的表达式
2. 星号表达式必须绑定到可迭代对象，否则会抛出TypeError
3. 拆包操作在嵌套结构中可以组合使用
4. **上下文行为差异**：
   - 函数定义中：`*args` 收集为**元组**
   - 变量赋值中：`*var` 收集为**列表**
   - 函数调用中：可拆包任何可迭代对象（不限于元组）
   - 序列构造中：可拆包任何可迭代对象（不限于元组）

## 6. 实际应用场景

- 将可迭代对象传递给函数作为多个参数
- 合并多个列表/元组/集合/字典
- 从序列中提取特定位置的元素，同时收集其余元素
- 跳过不需要的值
- 转换数据结构（如列表转集合） 