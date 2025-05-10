import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# 绘制点
# for i, value in enumerate(input_values):
#     x = input_values[i]
#     y = squares[i]
#     ax.scatter(x, y, s=200)
ax.scatter(input_values, squares, s=200)

ax.plot(input_values, squares, linewidth=3)

# 设置图表标题和坐标轴标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(labelsize=14)

# 设置样式
plt.show()