""" 
支持函数式编程的包: functools

1. functools.partial 冻结函数参数

2. functools.partialmethod 冻结方法参数

3. functools.reduce 函数

"""
import functools, unicodedata


from functools import partial
from operator import mul
triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))


nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'

print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))

print("\n")

def tag(name, *content, class_=None, **attrs):
    """
    Generate HTML tag
    """
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {key}="{value}"' for key, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        return '\n'.join(f'<{name}{attr_str}>{c}</{name}>' for c in content)
    else:
        return f'<{name}{attr_str} />'

print(tag)

picture = partial(tag, 'img', 'Picture', class_='pic-frame')
print(picture(src='wumpus.jpg'))

print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)

print("\n")







