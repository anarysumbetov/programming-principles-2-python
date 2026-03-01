import re

a = input()

x = re.findall("\\d", a)

for i in x:
    print(i, end=" ")