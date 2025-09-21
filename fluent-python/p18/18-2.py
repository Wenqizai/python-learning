""" 
把文件对象当成上下文管理器使用
"""

with open('mirror.py') as fp: # 打开文件绑定 fp
    src = fp.read(60)

print(len(src))

print(fp)

print(fp.closed, fp.encoding)

fp.read(10)