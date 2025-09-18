""" 
生成器表达式 ()
"""

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

result = [x * 3 for x in gen_AB()] # 列表推导式，即时生成

for i in result:
    print('->', i)

print("==" * 10)

result2 = (x * 3 for x in gen_AB()) # 生成器表达式，懒加载生成
print(result2)
for i in result2:
    print('->', i)