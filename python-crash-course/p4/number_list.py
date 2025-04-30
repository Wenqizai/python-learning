digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits))
print(max(digits))
print(sum(digits))

print("\n")

# 遍历中，不应该修改列表的值，结果不可控, python 不会报错， Java 会
for value in digits:
    del digits[0]
    print(value)
