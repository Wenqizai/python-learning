""" 
fibonacci 返回一个产生证书的生成器
"""
from collections.abc import Iterator
import itertools

def fibonacci() -> Iterator[int]:
    a, b = 0, 1 
    while True:
        yield a
        a, b = b, a + b

print(list(itertools.islice(fibonacci(), 10)))