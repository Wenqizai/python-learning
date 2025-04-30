responses = {}

# 设置一个标志，用于判断是否还有人要参与调查
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将响应存储在字典中
    responses[name] = response
    
    # 判断是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")

print("\n--- Poll Results ---")
