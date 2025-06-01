""" 
高阶函数: 接收函数为参数, 或者把函数作为结果返回的函数
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


def reverse(word):
    return word[::-1]

print(reverse('testing'))

print(sorted('hello, world'))

