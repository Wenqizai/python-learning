""" 
注解中可用的类型: Any 类型

Any 类型是所有类型的父类, 可以表示任何类型, 不推荐使用, 不利于类型工具检查
"""
import typing

def double(x): 
    return x * 2

# 类型提示
def double(x: typing.Any) -> typing.Any:
    return x * 2

# 类型检查工具拒绝以下函数
def double(x: object) -> object:
    return x * 2


class T1:
    pass

# 继承 T1 类
class T2(T1):
    pass

def f1(p: T1) -> None:
    # TODO document why this method is empty
    pass

o2 = T2()
f1(o2) # 有效, 里氏替换 T2 可以替换 T1, 说明 T2 是 T1 的子类


def f2(p: T2) -> None:
    pass
o1 = T1()
f2(o1) # 违背里氏替换原则, 类型检查工具拒绝 T1 类型


def f3(p: typing.Any) -> None:
    pass

o0 = object()
o1 = T1()
o2 = T2()

# 有效, Any 类型可以表示任何类型
f3(o0) 
f3(o1)
f3(o2)

# 返回值类型隐含为 Any 类型
def f4():
    pass

o4 = f4() # 有效, 返回值类型隐含为 Any 类型

# 有效, 返回值类型隐含为 Any 类型
f1(o4)
f2(o4)
f3(o4)






