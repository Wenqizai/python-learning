""" 
一个参数化注册装饰器
"""

registry = set()

def register(active=True):
    
    def decorate(func):
        print(f"running register(active={active})->decorate({func})")
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    
    return decorate

@register(active=False)
def f1():
    print("running f1()")

@register()
def f2():
    print("running f2()")

def f3():
    print("running f3()")

print(registry)

print(register()(f3)) # 装饰器工厂

print(registry)

print(register(active=False)(f2)) # 装饰器工厂

print(registry)

f1()
f2()
f3()

print(registry)
