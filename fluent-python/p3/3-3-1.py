""" 
使用匹配模式匹配处理映射
"""

from collections import OrderedDict

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")


b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
print(get_creators(b1))

# 这个例子说明 match / case 的匹配模式与 dict 的键顺序无关
b2 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())
print(get_creators(b2))

print(get_creators({'type': 'book', 'pages': 770}))

print(get_creators('Spam, spam, spam'))

