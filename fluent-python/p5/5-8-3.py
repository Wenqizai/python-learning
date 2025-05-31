""" 
模式匹配类实例: 位置类模式

通过 __match_args__ 查看类位置参数
"""
import typing 


class City(typing.NamedTuple):
    continent: str
    country: str
    name: str

# 查看类位置参数

print(City.__match_args__)


cities = [
    City('Asia', 'China', 'Shanghai'),
    City('Asia', 'China', 'Beijing'),
    City('Europe', 'France', 'Paris'),
    City('Europe', 'France', 'Lyon'),
    City('Europe', 'France', 'Lille'),
    City('North America', 'United States', 'Montreal'),
    City('North America', 'United States', 'Chicago'),
    City('South America', 'Argentina', 'Buenos Aires'),
    City('South America', 'Argentina', 'Rosario'),
    City('North America', 'United States', 'New York'),
    City('Europe', 'United Kingdom', 'London'),
]

def match_asian_cities_pos():
    """ 返回都是亚洲的城市 """
    results = []
    for city in cities:
        match city:
            case City('Asia'): # 位置匹配，第一个属性值是 Asia 
                results.append(city)
    return results

print(match_asian_cities_pos())


print("\n")

def match_asian_countries_pos():
    """ 返回亚洲的国家 """
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                results.append(country)
    return results

print(match_asian_countries_pos())



