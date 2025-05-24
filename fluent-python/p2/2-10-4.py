""" 
双端队列和其他队列

list 使用 .append 和 .pop 方法在列表头部添加和删除元素，相当于栈和队列使用
但是，在列表头部插入和删除元素的效率很低，因为需要移动列表中的其他元素

collections.deque 类（双向队列）是一个线程安全、可以快速从两端添加或删除元素的数据类型

线程安全的队列类：

无界队列：SimpleQueue
有界队列：Queue，后进先出队列, LifoQueue 优先级队, PriorityQueue


"""
from collections import deque

dq = deque(range(10), maxlen=10) # maxlen 是可选参数，指定队列允许的最大元素数量
print(dq)

print("--------------------------------")

dq.append(10) # 如果队列满了，append 会从另一端删除元素
print(dq)

print("--------------------------------")

dq.rotate(3) # 轮转， 当 n > 0 时，从右端取 n 个元素，放在左端，当 n < 0 时，从左端取 n 个元素，放在右端
print(dq)

dq.rotate(-4)
print(dq)

print("--------------------------------")

dq.appendleft(-1) # 在队列头部添加元素
print(dq)

dq.extend([11, 22, 33]) # 在队列尾部添加多个元素
print(dq)

dq.extendleft([10, 20, 30, 40]) # 在队列头部添加多个元素
print(dq)

