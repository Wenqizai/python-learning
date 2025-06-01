""" 
仅限位置参数
"""

def divmod(a, b, /):
    return a // b, a % b

print(divmod(10, 3))
# print(divmod(a=10, b=3)) # 会报错, 因为 divmod 的第一个参数是位置参数

def tag(name, content, /, class_=None, **attrs):
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

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class_': 'framed'}
print(tag(**my_tag)) # 报错 name 是位置参数, 不能通过关键字参数传入
