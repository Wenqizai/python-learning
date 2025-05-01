# 函数返回字典
def build_person(first_name, last_name):
    """ 返回一个字典， 其中包含有关一个人的信息 """
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person("jimi", "hendrix")
print(musician)

# 可选形参
def build_person_2(first_name, last_name, age=None):
    """ 返回一个字典， 其中包含有关一个人的信息 """
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person_2("jimi", "hendrix", age=27)
print(musician)

musician = build_person_2("jimi", "hendrix")
print(musician)

