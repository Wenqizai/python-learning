""" 
    把元组当作记录来使用
"""

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856'), ('USA', '21195855')]

for passport in sorted(traveler_ids): # 先按第一个字段排序，再按第二个字段排序
    # % 格式话运算符理解元组结构，把每一项当作不同的字段
    print('%s/%s' % passport)


# 元组拆包
# 元组拆包可以应用到任何可迭代对象上，唯一的限制是，被迭代的对象内元素数量必须与变量数量一致
# 元组拆包可以应用到嵌套元组上
for country, _ in traveler_ids:
    # _ 变量表示不关心的值，_ 变量名没有特殊含义，可以换成其他变量名
    # 一般习惯使用 _ 标识虚拟变量
    print(country)

