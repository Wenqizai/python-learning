""" 
  导入不同路径的包，需要模块化导入，以下可以参考 /python-learning/doc/python_import_guide.md
  需要运行模块化的指令：cd python-crash-course && python -m p8.modules.making_pizzas_module
"""
# 方法1: 使用绝对导入
# from p8 import pizza

# # 方法2：使用相对导入（仅在包内有效）
from .. import pizza

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

