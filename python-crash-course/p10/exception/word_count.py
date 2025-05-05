""" 
    异常处理: 多个文件
"""
from pathlib import Path

def count_words(path):
    """ 计算一个文件大致包含多少个单词 """
    try:
        # with path.open(mode='r', encoding='utf-8') as f:
        #     contents = f.read()
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
        
path = Path('resources/alice.txt')
count_words(path)


filesnames = ['resources/alice.txt', 'resources/siddhartha.txt', 'resources/moby_dick.txt', 'resources/little_women.txt']
for filename in filesnames:
    path = Path(filename)
    count_words(path)