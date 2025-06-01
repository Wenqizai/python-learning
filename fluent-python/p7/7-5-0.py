""" 
9 种可调用对象: 判断对象是否可调用使用内置函数 callable(obj)

1. 用户定义的函数: def 语句或 lambda 表达式

2. 内置函数: 如 len 或 time.strftime

3. 内置方法: 如 dict.get

4. 方法: 如类中定义的函数 str.lower

5. 类: 创建类时会调用 __new__ 方法, 然后调用 __init__ 方法

6. 类实例: 如果类定义了 __call__ 方法, 那么它的实例可以作为函数调用

7. 生成器函数: 如生成器表达式

8. 生成器表达式: 如 (item for item in iterable)

9. 协程: 如 async def 定义的协程函数. 调用原声协程函数会返回一个协程对象
"""

print(abs, str, 'Ni!')
# 判断对象是否可调用使用内置函数 callable
print([callable(obj) for obj in (abs, str, 'Ni!')])






