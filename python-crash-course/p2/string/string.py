# 转义字符
print("Hello\nWorld")
print("Hello\tWorld")

# 裁剪空白，返回新的值，不改变原来的值
python_ = " | Python | "
print(python_.strip())  # 两边裁剪
print(python_.lstrip()) # 左边裁剪
print(python_.rstrip()) # 右边裁剪

# 删除前缀
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))



