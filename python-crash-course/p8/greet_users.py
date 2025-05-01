# 形参传递 list
def greet_users(names):
    """ 向列表中的每位用户发出简单的问候 """
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)


# 在参数中修改传入的 list, 非函数实现
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# 在参数中修改传入的 list, 函数实现 (指针传递)
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
print_models(unprinted_designs, completed_models)
print(completed_models)
print(unprinted_designs)


# 在参数中传递 list 的副本
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs[:], completed_models) # 传递 unprinted_designs 的副本
print(unprinted_designs)
print(completed_models)

