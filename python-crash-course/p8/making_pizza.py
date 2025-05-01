# 导入函数, 需要在相同目录
""" 
    1. 导入所有函数 import module_name
    import pizza

    2. 导入单个函数 from module_name import function_name
    from pizza import make_pizza

    3. 使用as给函数指定别名 from module_name import function_name as fn
    from pizza import make_pizza as mp
    
    4. 导入所有函数，并指定别名 from module_name import * as fn
    from pizza import * as pizza
    
    5. 导入多个函数 from module_name import function_name1, function_name2
    from pizza import make_pizza, make_pizza2


    导入函数相当于将函数复制了一份到当前文件中，所以可以直接使用函数名调用，谨慎使用 import *
    如果导入所有函数会遇到重名问题，导致函数相互覆盖，需要使用 as 指定别名
"""
import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

print("--------------------------------")

import pizza as p

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

print("--------------------------------")

from pizza import *

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")



