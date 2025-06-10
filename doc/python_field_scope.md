# Python 变量作用域与关键字实践

本文档旨在阐明 Python 的变量作用域规则、赋值机制，并提供 `global` 和 `nonlocal` 关键字的最佳实践。

---

## 核心概念：LEGB 查找规则

Python 在查找变量时遵循一个明确的顺序，称为 **LEGB** 规则。这是一个从最内层到最外层的搜索路径：

1.  **L (Local) - 局部作用域**: 函数内部。每次函数调用都会创建一个新的局部作用域。这是搜索的第一站。
2.  **E (Enclosing) - 闭包作用域**: 存在于嵌套函数中，指外部（非全局）函数的作用域。如果一个函数在另一个函数内部定义，那么内部函数就可以访问外部函数的变量。
3.  **G (Global) - 全局作用域**: 模块的顶层。在.py文件中，所有在函数、类之外定义的变量都属于全局作用域。
4.  **B (Built-in) - 内建作用域**: Python 解释器启动时就存在的名称，如 `len()`, `str()`, `Exception` 等。这是搜索的最后一站。

**关键原则**：Python 会按 `L -> E -> G -> B` 的顺序查找变量。一旦找到，便立即停止搜索。

---

## 变量查找规则演示

以下代码清晰地展示了 LEGB 的查找顺序：

```python
# G (Global Scope)
g_var = "G: 我是全局变量"

def outer_func():
    # E (Enclosing Scope)
    e_var = "E: 我是闭包变量"

    def inner_func():
        # L (Local Scope)
        l_var = "L: 我是局部变量"
        
        # 1. 查找 l_var: 
        #    首先在局部(L)查找, 找到了 -> "L: 我是局部变量"
        print(f"查找 l_var: {l_var}")
        
        # 2. 查找 e_var: 
        #    在局部(L)没找到, 去上一层闭包(E)查找, 找到了 -> "E: 我是闭包变量"
        print(f"查找 e_var: {e_var}")

        # 3. 查找 g_var: 
        #    在局部(L)没找到, 在闭包(E)没找到, 去全局(G)查找, 找到了 -> "G: 我是全局变量"
        print(f"查找 g_var: {g_var}")

        # 4. 查找 len: 
        #    在 L, E, G 都没找到, 最后去内建(B)查找, 找到了 -> <built-in function len>
        print(f"查找 len: {len}")

    inner_func()

# outer_func()
# -- 输出 --
# 查找 l_var: L: 我是局部变量
# 查找 e_var: E: 我是闭包变量
# 查找 g_var: G: 我是全局变量
# 查找 len: <built-in function len>
```

---

## 赋值规则：默认创建局部变量

这是最容易引起混淆的地方：

> **当你在函数内部对一个变量进行赋值操作（`x = value`）时，Python 默认会在当前函数的局部作用域（L）中创建这个变量，除非已用关键字明确声明。**

-   如果只是**读取**一个变量，Python 会沿着 LEGB 路径去寻找。
-   但只要有**赋值**操作，该变量就会被视为**局部的**，这会"遮蔽"任何外部同名变量。

### 示例：
```python
x = "global"
def my_func():
    # 下面这行会报错 UnboundLocalError，而不是打印 "global"
    # 因为赋值操作 `x += " local"` 让 Python 在编译时就将 x 标记为局部变量，
    # 但在运行时尝试读取它以完成 `+=` 操作时，这个局部变量还未被定义。
    # print(x) 
    x += " local" 

# my_func() # 取消注释会报错
```

---

## 关键字与最佳实践

为了覆盖默认的赋值行为，我们使用 `global` 和 `nonlocal`。

### `global` 关键字

-   **作用**：在函数内部声明一个变量来自**全局作用域 (G)**。后续对该变量的赋值将直接修改全局变量本身，而不是创建局部变量。
-   **示例**：
    ```python
    count = 0
    def increment():
        global count
        count += 1
    
    increment()
    print(count) # 输出: 1
    ```
-   **最佳实践**：
    -   **尽量避免使用 `global`**。过度使用 `global` 会导致代码难以理解和维护。变量的值可以被任何调用了 `global` 的函数修改，使得状态追踪变得困难，也破坏了函数的封装性。
    -   **优先选择参数和返回值**。作为替代方案，应将状态作为参数传入函数，并通过返回值传出修改结果。这使得函数的输入输出非常明确。
        ```python
        # 更好的方式
        def increment_pure(c):
            return c + 1
        
        count = 0
        count = increment_pure(count)
        print(count) # 输出: 1
        ```

### `nonlocal` 关键字

-   **作用**：在**嵌套的内部函数**中，声明一个变量来自最近的**闭包作用域 (E)**。它用于修改外部（但非全局）函数的变量。
-   **示例**：
    ```python
    def make_counter():
        count = 0
        def counter():
            nonlocal count
            count += 1
            return count
        return counter

    c1 = make_counter()
    print(c1()) # 输出: 1
    print(c1()) # 输出: 2
    ```
-   **最佳实践**：
    -   `nonlocal` 是构建**闭包**和**需要维护状态的装饰器**的核心工具。它的使用场景比 `global` 更具针对性，通常也更合理。
    -   当你的设计模式（如工厂函数、带状态的装饰器）确实需要在嵌套函数间共享和修改状态时，`nonlocal` 是正确且必要的选择。

---

## 总结

1.  **明确边界**：函数的输入应来自参数，输出应通过 `return`。这是最清晰、最容易测试的模式。
2.  **谨慎使用 `global`**：把它当作最后的手段。如果发现自己需要频繁使用 `global`，这通常是重新思考程序结构的一个信号。
3.  **拥抱 `nonlocal`**：在编写闭包等高级函数式编程模式时，`nonlocal` 是实现其功能的关键。它使得函数可以封装和管理自身的状态，是 Python 强大功能的体现。 