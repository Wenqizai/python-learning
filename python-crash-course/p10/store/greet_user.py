from pathlib import Path
import json

filename = 'resources/remember_me.json'
path = Path(filename)

if path.exists():
    username = json.load(path.open(mode='r', encoding='utf-8'))
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    json.dump(username, path.open(mode='w', encoding='utf-8'))
    print(f"We'll remember you when you come back, {username}!")