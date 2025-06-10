""" 
标准库中的装饰器:  functools.lru_cache

lru_cache 可以通过参数 maxsize 设置缓存大小, 默认是 128
"""
import functools

@functools.lru_cache(maxsize=2**20, typed=True)
def costly_function(a, b):
    ...