# 字符串中使用变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name.title()} {last_name}" # f 代表 format，可以引用变量
print(full_name)
print(f"Hello, {full_name.title()}!")

