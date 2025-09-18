""" 
使用 itertools 模块生成等差数列
"""
import itertools

gen = itertools.count(1, 0.5)
print(next(gen))
print(next(gen))

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, 0.5))
print(list(gen))

print("==" * 10)

def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is None:
        return ap_gen 
    return itertools.takewhile(lambda n: n < end, ap_gen)
    

ap = aritprog_gen(0, 1, 3)
print(list(ap))

ap = aritprog_gen(0, 1/3, 1.5)
print(list(ap))



