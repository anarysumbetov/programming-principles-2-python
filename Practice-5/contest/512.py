import re

a = input()

x = re.findall("\d\d+", a)

for i in x:
    print(i, end=" ")