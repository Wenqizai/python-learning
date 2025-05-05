def get_formatted_name(first, last):
    """ 返回整洁的姓名 """
    full_name = f"{first} {last}"
    return full_name.title()

# 如果是两个同名的函数，后面的函数会覆盖前面的函数， 如果不想覆盖，可以给函数添加一个默认值参数
def get_formatted_name(first, last, middle=""):
    """ 返回整洁的姓名 """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

