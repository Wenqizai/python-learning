""" 
装饰器

标准库的装饰器: @cache, @lru_cache @singledispatch

装饰器: 
1. 装饰器通常会修改函数或方法的调用方式
2. 装饰器通常会返回一个修改后的函数或方法
3. 装饰器通常会使用 @decorator_name 语法糖来应用

对于 decorate 函数来说, 重要的是看它 return 的 func,
当定义

@decorate
def target():
    print("running target()")

相当于调用了

target = decorate(target)

所以 decorate 在函数定义时就会加载运行
"""
def decorate(func):
    print("running decorate()")
    return func

# 装饰器在函数定义时执行, 所以会打印 "running decorate()", 因为 decorate 返回了 target 函数, 所以 target() 会执行 target 函数
@decorate
def target():
    print("running target()")

target()
print(target) # <function target at 0x105195940>


print("########################")

def deco(func): 
    def inner(): 
        print("running inner()")
    return inner

# 这时候 tartget 函数已经被 inner 函数替换, 所以调用 target2() 会执行 inner(), 不会打印 "running target2()"
@deco
def target2():
    print("running target2()")

target2()
print(target2) # <function deco.<locals>.inner at 0x105195940>