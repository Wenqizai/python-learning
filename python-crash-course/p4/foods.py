my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods # 浅拷贝
friend_foods = my_foods[:] # 复制列表，深拷贝


my_foods.pop()
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

