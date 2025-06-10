""" 
闭包

闭包是函数式编程的重要特性, 闭包是指函数可以记住并访问它的词法作用域, 即使函数是在词法作用域之外调用的.

闭包的实现需要满足以下条件:
1. 函数内部定义了另一个函数
2. 内部函数访问了外部函数的变量
"""

class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))

print("-"*50)

def make_averager():
    series = [] # 自由变量

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    
    return averager # 返回内部函数, 形成闭包

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
