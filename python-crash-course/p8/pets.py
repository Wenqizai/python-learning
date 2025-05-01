# 函数定义 
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")

# 关键字实参, 顺序无关紧要
describe_pet(animal_type="dog", pet_name="willie")
describe_pet(pet_name="willie", animal_type="dog")


# 默认值
def describe_pet_2(pet_name, animal_type="dog"):
    """ 显示宠物的信息 """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_2(pet_name="willie")

# 如果实参有值，那么默认值会被覆盖
describe_pet_2(pet_name="harry", animal_type="hamster")



# 全默认值
def describe_pet_3(pet_name="harry", animal_type="dog"):
    """ 显示宠物的信息 """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet_3()

# 无参数， 且无默认值，或参数数量不匹配，运行报错
# describe_pet()
