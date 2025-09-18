""" 
等差数列
"""
class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.stop = end # None -> 无穷数列

    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.stop is None
        index = 0
        while forever or result < self.stop:
            yield result
            index += 1
            result = result_type(self.begin + self.step * index)


ap = ArithmeticProgression(0, 1, 3)
print(list(ap))


# 实现等差数列的函数
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = type(result)(begin + step * index)

ap = aritprog_gen(0, 1, 3)
print(list(ap))