from pathlib import Path
import json

filename = 'resources/remember_me.json'
path = Path(filename)


def greet_user():
    """ 问候用户 """
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        json.dump(username, path.open(mode='w', encoding='utf-8'))
        print(f"We'll remember you when you come back, {username}!")

def get_stored_username():
    """ 获取存储的用户名 """
    if path.exists():
        username = json.load(path.open(mode='r', encoding='utf-8'))
        return username
    return None

greet_user()