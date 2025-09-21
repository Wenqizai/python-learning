""" 
yield from: 重新实现chain
"""

# itertools.chain：实现迭代器链，从第一个序列迭代完全之后，然后迭代下一个序列
print('chain', "===" * 10)
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s = 'ABC'
r = range(3)
print(list(chain(s, r)))

print('yield from', "===" * 10)
def chain(*iterables):
    for it in iterables:
        yield from it
print(list(chain(s, r)))

