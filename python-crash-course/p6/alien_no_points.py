alien_0 = {'color': 'green', 'speed': 'slow'}

#print(alien_0['points']) # 获取不存在的值，会报错

# 使用 get() 访问值，可以指避免上述错误，没有指定返回值，默认是 None
points = alien_0.get('points')
print(points)

