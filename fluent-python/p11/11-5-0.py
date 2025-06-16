""" 
classmethod
staticmethod

"""

class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    
    @staticmethod
    def statmeth(*args):
        return args

print(Demo.klassmeth())
print(Demo.statmeth())

print(Demo.klassmeth('hello'))
print(Demo.statmeth('hello'))

