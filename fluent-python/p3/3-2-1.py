""" 
字典推导式
"""
dial_codes = [
    (880, 'Bangladesh'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (81, 'Japan'),
    (1, 'United States'),
    (64, 'New Zealand'),
    (44, 'United Kingdom'),
    (7, 'Russia'),
    (994, 'Azerbaijan'),
    (48, 'Poland'),
    (54, 'Argentina'),
    (351, 'Portugal'),
    (1, 'Canada'),
    (852, 'Hong Kong'),
    (81, 'Japan'),
    (82, 'South Korea'),
    (55, 'Brazil'),
    (986, 'Mongolia'),
    (212, 'Morocco'),
    (63, 'Philippines'),
]       

# 将元组列表转换为字典
country_dial = {country: code for code, country in dial_codes}
print(country_dial)



country_dial = {code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
print(country_dial)


