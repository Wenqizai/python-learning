""" 
构建嵌套列表
"""

# 创建新的列表：正确构建不同对象的嵌套列表
board = [['_'] * 3 for _ in range(3)]
print(board)

board[1][2] = 'X'
print(board)

# 同一个列表引用：错误做法, 构建的列表中每个元素都是对同一个列表的引用
weird_board = [['_'] * 3] * 3
print(weird_board)

weird_board[1][2] = 'O'
print(weird_board)

# 同一个列表引用：这样的做法也是创建同一个列表的引用
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)

board[2][0] = 'X'
print(board)

# 创建新的列表
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)

board[2][0] = 'X'
print(board)



