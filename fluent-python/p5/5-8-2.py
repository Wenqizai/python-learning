""" 
模式匹配类实例: 关键词类模式
"""
import typing 

class City(typing.NamedTuple):
    continent: str
    country: str
    name: str

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

# 返回都是亚洲的城市 
def match_asian_cities(): 
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=cc): # 这里cc是变量, 可以匹配任何值，并绑定到 country 变量
                results.append(city)
    return results


print(match_asian_cities())






