""" 
标准库中的装饰器:  functools.singledispatch

@singledispatch 标识处理 object 类型的基函数
@<<base>>.register(<<type>>) 为特定类型注册一个处理函数
"""
from functools import singledispatch
import html
from collections import abc
import numbers
import fractions
import decimal

def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

# 如果针对不同的入场, 改写生成的 html, 要么重写不同 htmlize 函数, 要么在 htmlize 函数中添加条件分支 if-else
# singledispatch 可以很好解决这些痛点
print(htmlize({1, 2, 3}))
print(htmlize(abs))
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(42))
print(htmlize(['alpha', 66, {3, 2, 1}]))

print('-' * 50)

@singledispatch
def htmlize(obj: object) -> str:
    content = html.escape(repr(obj))    
    return f'<pre>{content}</pre>'

@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace('\n', '<br>\n')
    return f'<p>{content}</p>'

@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

@htmlize.register
def _(n: numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'

@htmlize.register
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'

@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'

@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
    frac = fractions.Fraction(x).limit_denominator()
    return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'






