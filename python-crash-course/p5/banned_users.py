# 检查特定值是否在列表中
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
print('mushrooms' in requested_toppings)

# 检查特定值是否不在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


# 布尔表达式
game_active = True
can_edit = False