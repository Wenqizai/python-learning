""" 
使用匹配模式匹配处理映射
"""

food = dict(category='ice cream', flavor='vanilla', cost=199)

match food:
    case {'category': 'ice cream', **details}:
        print(f"Ice cream details: {details}")
    case {'category': 'ice cream', 'flavor': flavor, 'cost': cost}:
        print(f"Ice cream flavor is {flavor} and costs {cost} cents")
    case _:
        print("Unknown food")
