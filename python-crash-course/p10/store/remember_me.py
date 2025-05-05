from pathlib import Path
import json

filename = 'resources/remember_me.json'
path = Path(filename)

username = input("What is your name? ")
content = json.dumps(username)
path.write_text(content)


print(f"We'll remember you when you come back, {username}!")