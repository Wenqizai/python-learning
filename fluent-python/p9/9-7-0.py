""" 
nonlocal 关键字

nonlocal 关键字用于在嵌套函数中声明一个变量, 该变量是外部函数中的变量, 而不是局部变量.

nonlocal 关键字只能在嵌套函数中使用, 不能在全局作用域中使用.

"""


def make_averager():
    """ 不保存历史值 """
    count = 0
    total = 0

    def averager(new_value):
        count += 1 # 报错, count 有赋值操作, 被认为是局部变量
        total += new_value # 报错, total 有赋值操作, 被认为是局部变量
        return total / count
    
    return averager

avg = make_averager()
# print(avg(10))
# print(avg(11))
# print(avg(12))

print("-"*50)

def make_averager():
    """ 不保存历史值 """
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    
    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

print("-"*50)