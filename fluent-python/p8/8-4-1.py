""" 
鸭子类型
"""

class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Quack!')

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck) -> None:
    birdie.quack()

# Bird 没有函数
def alert_bird(birdie: Bird) -> None:
    birdie.quack()

# 都是有效调用, 类型提示, 不会运行报错
daffy = Duck()
alert(daffy)    
alert_duck(daffy)
alert_bird(daffy)





