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

# 打印表头
for index, column_header in enumerate(header_row):
    print(index, column_header)

# 提取最高气温和日期
highs = []
dates = []
for row in reader:
    high = int(row[5])
    highs.append(high)
    current_date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(current_date)
print(f"最高气温数据, 共: {len(highs)} 条， {highs}")

# 可视化最高气温
plt.style.use("seaborn-v0_8-paper")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")

# 设置图表标题和标签
ax.set_title("Daily High Temperatures, July 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
