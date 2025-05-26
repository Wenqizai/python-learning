""" 
使用 Unicode 排序算法排序

pyuca 是 Unicode Collation Algorithm 的 Python 实现，
可以不区分平台来排序

"""
import pyuca

collator = pyuca.Collator()

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits, key=collator.sort_key))
