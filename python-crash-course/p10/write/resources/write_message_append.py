"""
    追加写入文件 file
"""
from pathlib import Path

path = Path('resources/programming.txt')
if not path.exists():
    path.touch()
    
    
# 追加写入方法1：使用open()函数和'a'模式
with open('resources/programming.txt', 'a') as file:
    file.write('I love creating apps that can run in a browser.\n')
    file.write('I also love finding meaning in large datasets.\n')

# 追加写入方法2：使用pathlib的open()方法
with path.open(mode='a') as file:
    file.write('I love creating games.\n')
    file.write('I love creating mobile apps.\n')

# 追加写入方法3：先读取原内容，再合并写入
original_content = path.read_text()
new_content = original_content + 'This is appended text.\n'
path.write_text(new_content)

# 追加写入方法4：使用第三方库如pandas (对于数据处理)
# import pandas as pd
# df = pd.DataFrame({'data': ['new line 1', 'new line 2']})
# df.to_csv('resources/programming.txt', mode='a', header=False, index=False)





