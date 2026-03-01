import re

a = input()

x = re.findall("[A-Z]", a)

print(len(x))