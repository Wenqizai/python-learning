""" 
    序列模式匹配 match/case
    
    以下类型可以用序列模式匹配
    list, tuple, memoryview, array.array, range, collections.deque
"""

def handle_command(self, message):
    match message:
        case ["BEEPER", frequency, times]: # 第一项字符串 "BEEPER", 第二项任意绑定 frequency, 第三项任意绑定 times
            self.beep(times, frequency)
        case ["NECK", angle]: # 第一项字符串 "NECK", 第二项任意绑定 angle
            self.rotate_neck(angle)
        case ["LED", ident, intensity]: # 第一项字符串 "LED", 第二项任意绑定 ident, 第三项任意绑定 intensity
            self.leds[ident].set_brightness(ident, intensity)
        case ["LED", ident, r, g, b]: # 第一项字符串 "LED", 第二项任意绑定 ident, 第三项任意绑定 r, 第四项任意绑定 g, 第五项任意绑定 b
            self.leds[ident].set_color(r, g, b)
        case _:
            # raise 抛异常
            raise ValueError(f"Invalid command: {message}")

metro_areas = [
    ("Tokyo", "JP", 36.933, (35.681236, 139.770366)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.432607, -99.133209)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f"{'':15} | {'latitude':>9} | {'longitude':>9}")
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")

if __name__ == "__main__":
    main()

# match/case 上下文， str， bytes，bytearray 实例不作为序列处理
# match 会将这些类型作为原子值处理， 比如 987 会匹配 987， 但是不会拆分匹配 9 8 7
# 可以将这些转为元组处理
phone = "1234567890"
match tuple(phone):
        case ["1", *rest]: # 第一项字符串 "1"
            print("111")   
        case ["2", *rest]: # 第一项字符串 "2"
            print("222")
        case _: # 默认
            print("333")


# _符号，可以匹配相应位置上的任何一项，但是不绑定到变量的字， _可以多次出现
record = ['Shanghai', 'CN', 24.23, (31.23, 121.47)]
match record:
    case [name, _, _, (lat, lon) as location]:
        print(f"name: {name}, location: {location}")
    case _:
        print("Not a valid record")

# 类型检查，表示匹配到的是对应的类型，比如 str(name) 表示 name 是 str 类型
# record = [22, 'CN', 24.23, (31.23, 121.47)] # 第一项是 int 类型，会匹配到 Not a valid record
match record:
    case [str(name), _, _, (float(lat), float(lon))]:
        print(f"{name}: {lat}: {lon}")
    case _:
        print("Not a valid record")

# 通配符 *_, 表示匹配到的是任意多个项，但是不绑定到变量 
match record:
    case [str(name), *_, (float(lat), float(lon))]:
        print(f"{name}: {lat}: {lon}")
    case _:
        print("Not a valid record")

# 多个绑定 extra, extra 是一个列表
match record:
    case [str(name), *extra, (float(lat), float(lon))]:
        print(f"{name}: {lat}: {lon} : {extra}")
    case _:
        print("Not a valid record")       
        