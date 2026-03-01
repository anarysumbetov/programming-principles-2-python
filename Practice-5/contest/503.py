import re

s = input()
p = input()

x = re.finditer(p, s)

count = 0
for i in x:
    count += 1
print(count)