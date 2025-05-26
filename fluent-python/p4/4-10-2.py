""" 
支持 str 和 bytes 的双模式 API: os 函数中的 str 和 bytes
"""

import os

print(os.listdir('.'))

print("------------")

print(os.listdir(b'.'))
