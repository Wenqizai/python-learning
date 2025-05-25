""" 
处理编码/解码问题

SyntaxError: 加载模块时编码不符合预期抛出 SyntaxError
"""

# Python 3 默认使用 UTF-8 编码源码，Python 2 则默认使用 ASCII。
# 如果加载的 .py 模块中包含 UTF-8 之外的数据，而且没有声明编码，
# 那么将看到类似下面的消息。

# SyntaxError: Non-UTF-8 code starting with '\xe6' in file 4-5-3.py on line 6, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details



