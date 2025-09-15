""" 
生成器的工作原理

yield 关键词： 惰性上线延后生成值, 可以节省内存和 cpu 的循环浪费
"""

def gen_123():
    yield 1
    yield 2
    yield 3

print(gen_123)
print(gen_123())

for i in gen_123():
    print(i)


g = gen_123()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # StopIteration

print("==" * 10)

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

for c in gen_AB():
    print('->', c) # 第一次循环停留在 yield A 处，第二次循环停留在 yield B 处