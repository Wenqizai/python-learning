""" 
防御可变参数
"""

class TwilightBus:
    """ 让乘客销声匿迹的校车 """
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team) # ['Sue', 'Maya', 'Diana'], 函数的修改让原有列表也发生了改变

print("\n")

# 正确应当是类独自维护列表

class TwilightBus:
    """ 让乘客销声匿迹的校车 """
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team) # ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']




