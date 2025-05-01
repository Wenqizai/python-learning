# 可变形参可以传入任意数量的键值对 （**形参，表示传入的是字典， *形参，表示传入的是元组）
def build_profile(first, last, **user_info):
    """ 创建一个字典，其中包含我们知道的有关用户的一切 """
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)




