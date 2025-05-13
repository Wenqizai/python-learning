import requests
import plotly.express as px 
import json

# 读取 Json 文件
with open('data/github_python_popularity.json', 'r') as f:
    response_dict = json.load(f)

# 处理结果
print(f"Complete results: {not response_dict['incomplete_results']}")

# 处理有关仓库的信息
repo_dicts = response_dict['items']

repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # 将仓库名转为链接
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 创建悬浮文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_texts.append(f"{owner} : {description}")

# 可视化
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, 
             y=stars, 
             title=title,
             labels=labels,
             hover_name=hover_texts
             )

# 设置持久悬浮模式
fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

fig.update_traces(
    marker_color='SteelBlue',
    marker_opacity=0.6
)

# 启用持久悬浮
fig.show()