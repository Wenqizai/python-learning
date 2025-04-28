favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")


# 使用 get() 访问值，可以指定默认值
language = favorite_languages.get('jack', 'No favorite language.')
print(language)


# 遍历字典
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# 遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())
print(f'\n{favorite_languages.keys()}') # dict_keys(['jen', 'sarah', 'edward', 'phil'])

# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language.title())
print(f'\n{favorite_languages.values()}') # dict_values(['python', 'c', 'ruby', 'python'])


# 按照特定顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()): # 按照字母顺序排序
    print(f"{name.title()}, thank you for taking the poll.")


# 遍历字典中的所有值，并去重
print(f'\nThe following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())


# 嵌套
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


