""" 
多重继承和方法解析顺序
"""
from diamond import A

class U():
    def ping(self):
        print(f'{self}.ping() in U')
        super().ping()

class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() in LeafUA')
        super().ping()

u = U()
# u.ping() # 报错, object 没有 ping 方法
print()

leaf2 = LeafUA()
leaf2.ping()