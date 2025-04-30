# 待验证用户列表
unconfirmed_users = ['alice', 'brian', 'candace']
# 已验证用户列表
confirmed_users = []

# 从待验证用户列表中，依次取出用户，并添加到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    