from die import Die
import plotly.express as px

# 创建1个D6
die_1 = Die()
# 创建1个D10
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 打印结果
print(results)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
title = "Results of rolling One D6 and One D10 Dice 50000 times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels) # 直方图
# fig = px.scatter(x=poss_results, y=frequencies, title=title, labels=labels) # 散点图
# fig = px.line(x=poss_results, y=frequencies, title=title, labels=labels) # 折线图

# 设置x轴刻度, 刻度为1
fig.update_layout(xaxis_dtick=1)

fig.show()

# 保存文件
fig.write_html("results/die_visual_d6d10.html")