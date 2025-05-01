# 返回值
def get_formatted_name(first_name, last_name):
    """ 返回整洁的姓名 """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)


# Python if 空字符串 为 True
# 以下为可选形参的函数
def get_formatted_name_2(first_name, last_name, middle_name=""):
    """ 返回整洁的姓名 """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_2("jimi", "hendrix")
print(musician)

musician = get_formatted_name_2("jimi", "hendrix", "lee")
print(musician)


