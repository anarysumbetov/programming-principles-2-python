import re

a = input()

x = re.search(r"Name: (.*), Age: (\d+)", a)

print(x.group(1), x.group(2))