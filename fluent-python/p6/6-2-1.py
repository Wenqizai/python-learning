""" 
变量不是盒子，而是便利贴，引用
"""

a = [1, 2, 3]
b = a
a.append(4)
print(b)

class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()
y = Gizmo() * 10 # 先创建一个临时对象，然后乘以10，发现乘法报错，但是这时对象已经创建了

