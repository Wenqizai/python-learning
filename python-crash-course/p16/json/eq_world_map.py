import plotly.express as px
from eq_explore_data import lons, lats, titles, mags, places
import pandas as pd

    
# 方法1: 使用 plotly.express 绘制散点图
# fig = px.scatter(
#     x=lats,
#     y=lons,
#     labels={'x':'Longitude', 'y':'Latitude'},
#     range_x=[-200, 200],
#     range_y=[-90, 90],
#     width=800,
#     height=800,
#     title='Global Earthquakes',
# )

# 方法2: 使用 pandas 创建数据框
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags, places),
    columns=['lon', 'lat', 'title', 'mag', 'place']
)
data.head()
fig = px.scatter(
    data,
    x='lon',
    y='lat',
    hover_name='title',
    hover_data=['mag', 'place'],
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='Global Earthquakes',
    size='mag',
    size_max=10,
    color='mag',
    color_continuous_scale='redor',
)

# print(px.colors.named_colorscales())

fig.write_html('eq_data/global_earthquakes.html')
fig.show()




