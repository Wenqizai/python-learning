from pathlib import Path
import json

# 将数据作为字符串读取
# path = Path("eq_data/eq_data_1_day_m1.json")
path = Path("eq_data/eq_data_30_day_m1.json")

try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)
        
# 将数据转换为更易于阅读的版本
path = Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4) # 格式化输出
path.write_text(readable_contents)


# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']

print(len(all_eq_dicts))


# 提取地震的震级
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])

# 提取位置数据
mags, titles, lons, lats, places = [], [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    place = eq_dict['properties']['place']
    
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
    places.append(place)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

