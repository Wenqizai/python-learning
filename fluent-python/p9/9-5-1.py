""" 
变量作用域规则

全局作用域: 在类/函数之外声明的变量
局部作用域: 在类/函数内部声明的变量 

"""
import dis
b = 6 # 全局变量

def f1(a):
    print(a)
    print(b)

f1(3) # 局部变量a, 全局变量b

def f2(a):
    """  print(b) 执行报错, 下面的代码 b = 9 对 b 重新赋值, 在编译时会把 b 当成局部变量, print(b) 时发现局部变量 b 未定义 """
    print(a)
    print(b) # UnboundLocalError: cannot access local variable 'b' where it is not associated with a value
    b = 9

# f2(3)

def f3(a):
    """ 使用 global 声明 b 为全局变量 """
    global b
    print(a)
    print(b)
    b = 9

f3(3)
print(b)

print("-"*50)

# 字节码对比
print(dis.dis(f1))

print("-"*50)

print(dis.dis(f2))

print("-"*50)

print(dis.dis(f3))
