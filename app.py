# print("Hello World")

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")


# === 变量 ===
# character_name = "Tom"
# character_age = 55
# is_male = True # False

# print("Threa once was a man named ", character_name, ", ")
# print("He was ", character_age, " years old. ")

# character_name = "Mike"
# character_age -= 10
# print("He really liked the name ", character_name, ". ")
# print("but don't like being ", character_age, ". ")


# === String ===
# print("Hello\nWorld")
# phrase = "Hello World"
# print(phrase + " is good")
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# # print(phrase[20]) # IndexError: string index out of range
# print(phrase.index("World"))
# # print(phrase.index("x")) # ValueError: substring not found
# print(phrase.replace("Hello", "Bye")) # new string
# print(phrase)

# === Numbers ===
# print(2)
# print(-2.33)
# print(2 + 2)
# print(1.5 * 2)
# print(3 * (4 + 5))
# print(10 % 3)
# print(10 / 3)
#
# my_num = 5
# print(my_num)
#
# print(str(my_num) + " is my favorite number") # covert to string
# print(str(5) + "1")
#
# my_num = -5
# print(abs(my_num))
# print(pow(3, 2))
# print(max(3, 5))
# print(min(3, 5))
# print(round(3.2))
# print(round(3.5))
#
# from math import *
# print(floor(3.7))
# print(sqrt(36))
# print(int(sqrt(36))) #

# === Input ===
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + ", you are " + age)

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# # print(num1 + num2) # just a string append
# # print(int(num1) + int(num2)) # print(num1 + num2)
# print(float(num1) + float(num2)) # print(num1 + num2)

# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)


# === list ===
# friends = ["Kevin", 2, "Jim", "Oscar", False] # 混合类型
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# print(friends[0])
# # print(bool(friends[0]))
# print(friends[-1]) # 从后往前
# print(friends[-2])
# print(friends[1:3])
# print(friends[1:])
#
# friends[0] = "Mike"
# print(friends[0:])

# lucky_numbers = [4, 8, 15, 16, 23, 42]
# # friends.extend(lucky_numbers)
# print(friends)
# friends.append("Creed")
# print(friends)
# friends.insert(2, "Kelly")
# print(friends)
# friends.remove("Jim")
# print(friends)
# print(friends.pop())
# print(friends)
# friends.append("Oscar")
# print(friends)
# print(friends.index("Oscar"))
# # print(friends.index("ACC")) # ValueError: 'ACC' is not in list
# print(friends.count("Oscar"))
# friends.sort()  # 混合类型排序报错
# print(friends)
#
# lucky_numbers.sort()
# print(lucky_numbers)
# lucky_numbers.reverse()
# print(lucky_numbers)

# === Tuple ===
# coordinates = (4, 5)  # 不可修改
# print(coordinates[0])
# coordinates[0] = 10 #  TypeError: 'tuple' object does not support item assignment

# === Functions ===
# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age))
#     print("Next line")
#
# print("Top")
# say_hi("Tim", 25)
# print("Bottom")

# === return statement ===
# def cube(num):
#     return num * num * num
#     # print("This is not printed") # 不会执行, 也不会报错
#
# result = cube(4)
# print(cube(3))
# print(result)

# === If statement ===
# is_male = input("Are you a male? 1 for yes, 0 for no: ")
# is_male = int(is_male)
# is_tall = True
#
# # 操作符 or and not
# if is_male == 1 or is_tall:
#     print("You are a male or tall or both")
# elif is_male == 0 and is_tall:
#     print("You are not a male and tall")
# elif is_male == 0 and not is_tall:
#     print("You are not a male but not tall")
# else:
#     print("Unknown")

# === Compare ===
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(3, 40, 5))

# === 2 Calculator ===
# num1 = float(input("Enter first number: "))
# operator = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "/":
#     print(num1 / num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "%":
#     print(num1 % num2)
# else:
#     print("Invalid operator")

# === Dictionary ===
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions)
print(monthConversions.get("Jan", "Not a valid key"))
print(monthConversions["Jan"])











