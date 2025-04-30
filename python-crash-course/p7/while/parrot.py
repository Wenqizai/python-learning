prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# 使用 break 跳出循环
message = ""
while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        break
    print(message)

print("\nThank you for playing!")


# 使用标志跳出循环
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

