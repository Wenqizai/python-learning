""" 
精度问题，导致 x != +x

"""

import decimal

ctx = decimal.getcontext()
ctx.prec = 40

one_third = decimal.Decimal('1') / decimal.Decimal('3')
print(one_third)
print(+one_third)
print(one_third == +one_third)

ctx.prec = 28 # 精度 28 时， one_third == +one_third 为 False
print(one_third == +one_third)
print(+one_third)
