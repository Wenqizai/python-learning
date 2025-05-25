""" 
自动处理缺失的键

1. 普通 dict 获取 defaultdict
2. 实现 __missing__ 方法


defaultdict 的 default_factory 仅为 __getitem__ 提供默认值，其他方法用不到。例如，dd 是一个
defaultdict 对象，如果没有键 k，那么 dd[k] 将调用 default_factory 创建默认值，但是 dd.get(k) 依然返回
None，而且 k in dd 也返回 False。
"""

import collections
import re
import sys

WORD_RE = re.compile(r'\w+')

# 默认位 list 的构造函数
index = collections.defaultdict(list)

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

# 以字母顺序打印出单词出现的位置
for word in sorted(index, key=str.upper):
    print(word, index[word])