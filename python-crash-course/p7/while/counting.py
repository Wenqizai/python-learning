current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\n")

# 使用 continue 跳过当前循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


# 死循环
while True:
    print("\n")
    print("Enter 'quit' to end the program.")

    
