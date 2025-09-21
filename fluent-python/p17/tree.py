""" 
树形结构的遍历
"""

def tree(cls):
    yield cls.__name__, 0 # 两个参数
    for sub_cls in cls.__subclasses__():
        yield sub_cls.__name__, 1

def display(cls):
    for cls_name, level in tree(cls):
        indent = ' ' * 4 * level
        print(indent + cls_name)

if __name__ == '__main__':
    display(BaseException)