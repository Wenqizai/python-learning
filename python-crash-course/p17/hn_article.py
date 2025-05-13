import requests
import json

""" 
    获取 hacker-news 的热门文章，kids 是评论 id，descendants 是评论数
"""

# 执行 API 调用并存储响应 
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
response = requests.get(url)
print(f"Status code: {response.status_code}")

# 处理有关每篇文章的信息
response_dict = response.json()
readable_file = 'data/readable_hn_article.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

