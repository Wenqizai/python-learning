magicians = ['alice', 'david', 'carolina']

# 遍历列表
for magician in magicians:
    print(magician + '\n')

magicians = ['alice', 'carolina', 'david']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# 这个 for 循环结束后，magician 的值为 carolina，取遍历的最后一个值
print(f"I can't wait to see your next trick, {magician.title()}.\n")

print(f"Thank you, everyone. That was a great magic show!")


# 无必要的缩进
message = "Hello Python world!"
#  print(message) # 缩进错误，编译报错

print("########################")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print(f"Thank you, everyone. That was a great magic show!") # 缩进了，在循环内执行 




