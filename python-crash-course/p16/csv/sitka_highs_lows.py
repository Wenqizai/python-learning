from pathlib import Path
import csv
import matplotlib.pyplot as plt
import datetime as datetime

# 读取数据
# path = Path("weather_data/sitka_weather_07-2018_simple.csv")
path = Path("weather_data/sitka_weather_2018_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 提取最高气温和最低气温
highs = []
lows = []
dates = []
diffs = []  # 新增：存储温度差值        

for row in reader:
    current_date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(current_date)
    high = int(row[5])
    highs.append(high)
    low = int(row[6])
    lows.append(low)
    diffs.append(low + (high - low) / 2)  # 计算温度差值

print(highs)
print(lows)
print(dates)

# 可视化最高气温和最低气温
plt.style.use("seaborn-v0_8-paper")
fig, ax = plt.subplots()

ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)

# 填充颜色
ax.fill_between(dates, highs, lows, facecolor="green", alpha=0.5)

# 添加温度差值曲线和标记点
ax.plot(dates, diffs, c="purple", alpha=0.7, label="Temperature Difference")
ax.scatter(dates, diffs, c="purple", s=20, alpha=0.7)

# 设置图表标题和标签
ax.set_title("Daily High and Low Temperatures, 2018", fontsize=24)
ax.set_xlabel("Date", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)
ax.legend(fontsize=12)  # 添加图例

plt.show()
