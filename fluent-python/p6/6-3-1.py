""" 
== 和 is 之间选择

== 比较两个对象的值是否相等
is 比较两个对象的标识是否相

is 运算符比 == 运算符速度更快，因为它不能重载，所以 Python 不用考虑运算符重载的多种情况。

x is None
x is not None
"""

END_OF_DATA = object()

def traverse(node):
    if node is END_OF_DATA:
        return