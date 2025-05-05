""" 
    静默异常: pass 
"""
from pathlib import Path

def count_words(path):
    """ 计算一个文件大致包含多少个单词 """
    try:
        # with path.open(mode='r', encoding='utf-8') as f:
        #     contents = f.read()
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass # 什么都不做
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")
        
path = Path('resources/alice.txt')
count_words(path)

path = Path('resources/siddhartha.txt')
count_words(path)


