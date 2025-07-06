""" 
多重继承和方法解析顺序
"""

class Root:
    def ping(self):
        print(f'{self}.ping() in Root')

    def pong(self):
        print(f'{self}.pong() in Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'

class A(Root):
    def ping(self):
        print(f'{self}.ping() in A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in A')
        super().pong()

class B(Root):
    def ping(self):
        print(f'{self}.ping() in B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in B')
 
class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() in Leaf')
        super().ping()

    def pong(self):
        print(f'{self}.pong() in Leaf')
        super().pong()


leaf1 = Leaf()
leaf1.ping()
print()
leaf1.pong()

print() 

print(Leaf.__mro__) # 元组, 按照方法解析顺序列出各个超类