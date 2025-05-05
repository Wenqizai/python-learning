""" 
    使用 json 存储数据
    
    1. 使用 json.dumps() 将数据存储为 json 格式 ( 返回字符串 )
    2. 使用 json.dump() 将数据存储为 json 格式 ( 写入文件 )
    3. 使用 json.load() 将数据从 json 格式加载到内存中 ( 读取文件 )
    4. 使用 json.loads() 将数据从 json 格式加载到内存中 ( 读取字符串 )
"""

from pathlib import Path
import json

filename = 'resources/numbers.json'
path = Path(filename)

# 1. 读取 json 字符串
content = path.read_text()
numbers = json.loads(content)
print(numbers)

# 2. 读取 json 文件
numbers = json.load(path.open(mode='r', encoding='utf-8'))
print(numbers)

