import re

a = input()

x = re.findall("\w+", a)
print(len(x))