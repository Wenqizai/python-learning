# 函数标准

""" 
    1. 函数名应该使用小写字母和下划线，不要使用大写字母和下划线
    2. 函数名应该使用动词开头，如 get_name, calculate_total
    3. 函数名应该使用小写字母和下划线，不要使用大写字母和下划线
"""

# import 放在开头
import pizza as p

# 给形参指定默认值时，等号两边不要有空格(函数调用时，也是遵循这个规则，等号两边不要有空格)
def function_name(parameter_name='default_value'):
    print(parameter_name)
    
# 适当利用缩进，增加可读性
def function_name(parameter_0, parameter_1, parameter_2,
                  parameter_4, parameter_5, parameter6):
    print("end")
