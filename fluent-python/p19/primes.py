""" 
一个质数检测函数
"""
import math
import time

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


NUMBERS = [
    2,
    3333333333333333,
    4444444444444444,
    5555555555555555,
    6666666666666666,
    142702110479723 , 
    7777777777777777,
    299593572317531 , 
    9999999999999999,
    3333333333333301,  
    3333335652092209,
    4444444488888889,
    4444444444444423,  
    5555553133149889,
    5555555555555503,  
    6666666666666719,  
    6666667141414921,
    7777777536340681,
    7777777777777753,  
    9999999999999917,  
]

# 测试大数质数检测的耗时
# test_number = 5_000_111_000_222_021

# print(f"检测数字: {test_number}")
# print("开始检测...")

# start_time = time.time()
# result = is_prime(test_number)
# end_time = time.time()

# elapsed_time = end_time - start_time

# print(f"检测结果: {result}")
# print(f"耗时: {elapsed_time:.6f} 秒")
