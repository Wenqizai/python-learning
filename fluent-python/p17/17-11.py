""" 
yield from: 从子生成器中产出，把一个生成器的工作委托给一个子生成器
"""

# 没有 yield from 之前
from unittest import result


def sub_gen():
    yield 1.1
    yield 1.2

def gen():
    yield 1
    for i in sub_gen():
        yield i
    yield 2

for x in gen():
    print(x)

# 改造成 yield from
print("## yield from", "===" * 10)
def gen2():
    yield 1
    yield from sub_gen()
    yield 2

for x in gen2():
    print(x)

# yield from 获取子生成器的返回值
print("## yield from 获取子生成器的返回值", "===" * 10)
def sub_gen():
    yield 1.1
    yield 1.2
    return "Done!"


def gen3():
    yield 1
    result = yield from sub_gen()
    print('<--', result)
    yield 2


for x in gen3():
    print(x)
