""" 
模式匹配类实例: 简单类模式
"""
args = ['123', '456', '789', (10.0, 20.0)]
match args:
    # 简单类, 第一项是str, 最后一项是元组, 而且是 float float
    case [str(name), _, _, (float(lat), float(lon))]:
        print(f"{name} {lat} {lon}")

# case float: 可以匹配任何对象，因为 Python 把 float 看成匹配对象绑定的变量 
# case float(): 只能匹配 float 类型 
match args:
    case float():
        print(f"float(): {args}")
    case float: # 这个可能导致bug
        print(f"float: {args}")


