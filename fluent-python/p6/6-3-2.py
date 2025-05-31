""" 
元组的相对不可变性

元组与多数 Python 集合（列表、字典、集合等）一样，保存的是对象的引用。

如果元组保存的引用是不可变的，那么这个元组就是不可变的。

"""

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)

print(id(t1[-1]))
print(id(t2[-1]))

t1[-1].append(99)
print(t1)
print(t2)

print(id(t1[-1]))
print(id(t2[-1]))

print(t1 == t2)