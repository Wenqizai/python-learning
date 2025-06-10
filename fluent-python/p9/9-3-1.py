""" 
Python 何时执行装饰器

装饰器关键性质: 被装饰的函数定义之后会立即执行, 通常在导入/加载模块时执行

"""

registry = []

def register(func):
    print(f"running register({func})")
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")

@register
def f2():
    print("running f2()")

def f3():
    print("running f3()")

def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()
    