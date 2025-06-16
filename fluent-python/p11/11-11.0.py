""" 
__slots__ 节省空间

定义一个名为 __slots__ 的类属性，它会告诉 Python 不要使用字典， 而是使用序列形式存储属性名称。
"""

class Pixel: 
    __slots__ = ('x', 'y')

p = Pixel()
p.x = 10
p.y = 20
print(p.x, p.y)

# print(p.__dict__) # AttributeError: 'Pixel' object has no attribute '__dict__'
# p.color = 'red' # AttributeError: 'Pixel' object has no attribute 'color'

print("-" * 50)

# 子类继承了 __slot__
class OpenPixel(Pixel):
    pass

op = OpenPixel()
print(op.__slots__)
print(Pixel.__dict__)

op.x = 8
print(Pixel.__dict__)

op.color = 'red'
print(Pixel.__dict__)

print("-" * 50)

# 子类继承了 __slot__, 并加入了 color
class ColorPixel(Pixel):
    __slots__ = ('color',)

cp = ColorPixel()
# print(cp.__dict__) # AttributeError: 'ColorPixel' object has no attribute '__dict__'
cp.x = 2
cp.color = 'blue'
# cp.flavor = 'banana' # AttributeError: 'ColorPixel' object has no attribute 'flavor'
print(cp.__slots__)
