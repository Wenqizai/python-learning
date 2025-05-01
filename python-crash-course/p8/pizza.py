# 传递可变形参 （**形参，表示传入的是字典， *形参，表示传入的是元组）
def make_pizza(*toppings): # * 形参名 表示创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    """ 打印顾客点的所有配料 """
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# 传递的形参是数组，意味着可以遍历打印
def make_pizza(*toppings):
    """ 概述要制作的披萨 """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")
        
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# 可变参数与其他参数共用，可变参数必须放在最后, 而且一个函数只可以定义一个可变参数
def make_pizza(size, *toppings):
    """ 概述要制作的披萨 """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")
        
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


