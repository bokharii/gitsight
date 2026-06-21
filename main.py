from pathlib import Path

print("hello world")

with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
