import array

symbols = '$¢£¥€¤'

# 生成器表达式, 构建元组
tupleArr = tuple(ord(symbol) for symbol in symbols)
print(tupleArr)

# array 构造函数
# 构建更节省内存的数组， 类型码为 'I'， 即无符号整数
array = array.array('I', (ord(symbol) for symbol in symbols))
print(array)
print(array[0])

# 这种方式不用构建整个列表， 节省内存
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
