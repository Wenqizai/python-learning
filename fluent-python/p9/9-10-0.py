""" 
参数化装饰器
"""
registry = []

def register(func):
    print(f"running register {func}")
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

print("running main()")
print(f"registry -> {registry}")
f1()



