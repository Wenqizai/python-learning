# 多行 prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# 使用 int() 来获取数值输入
height = input("How tall are you, in inches? ")
height = int(height) # 将字符串转换为整数

if height >= 36:
    print("\nYou're tall enough to ride!")
    