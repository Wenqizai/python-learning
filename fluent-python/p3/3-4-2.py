""" 
Re-learning Python index0.py
"""

import re 
import sys 

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)

            # 这样写不完美，仅作演示
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

            # 相比上一种写法，setdefault 更简洁， 效率更高
            index.setdefault(word, []).append(location)

            

# 以字母顺序打印出单词出现的位置
for word in sorted(index, key=str.upper):
    print(word, index[word])
    

