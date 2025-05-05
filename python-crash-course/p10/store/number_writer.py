""" 
    使用 json 存储数据
    
    1. 使用 json.dumps() 将数据存储为 json 格式 ( 返回字符串 )
    2. 使用 json.dump() 将数据存储为 json 格式 ( 写入文件 )
    3. 使用 json.load() 将数据从 json 格式加载到内存中 ( 读取文件 )
    4. 使用 json.loads() 将数据从 json 格式加载到内存中 ( 读取字符串 )
"""
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'resources/numbers.json'
path = Path(filename)
if not path.exists():
    path.touch()
    
# 1. 存储 json 文件
with path.open(mode='w', encoding='utf-8') as f:
    json.dump(numbers, f)

# 2. 存储 json 字符串
content = json.dumps(numbers)
print(content)
path.write_text(content)




