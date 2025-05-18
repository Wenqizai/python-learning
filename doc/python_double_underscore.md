# Python 双下划线使用指南

## 1. 特殊方法（魔术方法）

特殊方法是 Python 中最重要的双下划线用法，它们定义了对象的基本行为。

### 1.1 常用特殊方法

```python
class Example:
    def __init__(self): pass      # 构造函数
    def __del__(self): pass       # 析构函数
    def __str__(self): pass       # 字符串表示
    def __repr__(self): pass      # 开发者字符串表示
    def __len__(self): pass       # 长度
    def __getitem__(self): pass   # 索引访问
    def __setitem__(self): pass   # 索引赋值
    def __iter__(self): pass      # 迭代器
    def __next__(self): pass      # 下一个元素
```

### 1.2 运算符重载

```python
class Vector:
    def __add__(self, other): pass    # +
    def __sub__(self, other): pass    # -
    def __mul__(self, other): pass    # *
    def __eq__(self, other): pass     # ==
    def __lt__(self, other): pass     # <
```

## 2. 名称改写（Name Mangling）

用于创建"私有"属性，主要用于避免子类属性名冲突。

```python
class Parent:
    def __init__(self):
        self.__private = 1  # 会被改写为 _Parent__private

class Child(Parent):
    def __init__(self):
        self.__private = 2  # 会被改写为 _Child__private
```

## 3. 内置变量

Python 提供了一些内置的双下划线变量：

```python
__name__    # 模块名
__file__    # 文件路径
__doc__     # 文档字符串
__dict__    # 对象的属性字典
__class__   # 对象的类
```

## 4. 使用规范

### 4.1 命名约定

1. `__xxx__`: 特殊方法和内置变量
2. `__xxx`: 名称改写（私有属性）
3. `_xxx`: 内部使用的变量/方法（单下划线）

### 4.2 最佳实践

1. 只在实现特殊方法时使用双下划线
2. 需要"私有"属性时使用单前导下划线
3. 避免自定义双下划线开头的变量名
4. 遵循 Python 的命名约定

### 4.3 注意事项

1. 双下划线不是真正的私有机制
2. 名称改写可能导致调试困难
3. 过度使用名称改写会降低代码可读性
4. 优先使用单下划线表示内部使用

## 5. 实际应用示例

### 5.1 实现序列类型

```python
class MySequence:
    def __init__(self):
        self._items = []
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
```

### 5.2 实现上下文管理器

```python
class MyContext:
    def __enter__(self):
        print("进入上下文")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文")
```

## 6. 总结

1. 双下划线主要用于特殊方法和名称改写
2. 特殊方法让自定义类可以像内置类型一样工作
3. 名称改写提供了一种避免命名冲突的机制
4. 遵循 Python 的命名约定和最佳实践
5. 优先使用更简单的单下划线约定 