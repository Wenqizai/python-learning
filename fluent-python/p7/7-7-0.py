""" 
从位置参数到仅限关键字参数: 仅关键词参数
"""

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


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))

print(tag('p', 'hello', id=33))

print(tag('p', 'hello', 'world', class_='sidebar'))
print(tag(content='testing', name="img"))

print("\n")

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class_': 'framed'}
print(tag(**my_tag)) # my_tag 前面加 **, 字典中的所有项作为参数依次传入, 同名键绑定对应的具名参数上


def f(a, *, b):
    return a, b

print(f(1, b=2))
print(f(1, 2)) # 会报错, 因为 b 是仅限关键字参数, 必须显式传入

