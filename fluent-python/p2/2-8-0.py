""" 
    使用 + 和 * 处理序列

    注意：+ 和 * 都遵循这个原则：
        1. 不修改原有的操作对象，而是构建新的序列；
        2. + 处理的序列都是同种类型的序列
        3. * 的第二个操作数必须是整数
"""

l = [1, 2, 3]
print(l)

l = l + [4, 5, 6]
print(l)

l = l * 3
print(l)

sl = ['a', 'b', 'c']
# print(sl * l) # 报错：TypeError: can't multiply sequence by non-int of type 'list'

print([[]] * 3)

