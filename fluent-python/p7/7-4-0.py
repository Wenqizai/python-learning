""" 
匿名函数: lambda 表达式

lambda 函数的主体智能是纯粹的表达式, 主体中不能有 while, try 等 Python 语句, = 是赋值语句, 不能用于 lambda 表达式
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word: word[::-1])





