""" 
    获取 hacker-news 的热门文章 id，并拉取相关文章 url
"""

import requests
import json

# 执行 API 调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
print(f"Status code: {response.status_code}")

# 写入 json 文件
with open('data/hn_submissions.json', 'w') as f:
    json.dump(response.json(), f, indent=4)

# 处理有关每篇文章的信息
submission_ids = response.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # 对于每篇文章，都执行一个 API 调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    response = requests.get(url)
    print(f"id: {submission_id}\tstatus: {response.status_code}")
    response_dict = response.json()
    

    # 对于每篇文章，都创建一个字典
    submission_dict = {
        'title': response_dict['title'],
        'link': f"http://news.ycombinator.com/item?id={submission_id}",
        'html_url': response_dict.get('url', ''),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=lambda x: x['comments'], reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")
    print(f"Relevant link: {submission_dict['html_url']}")