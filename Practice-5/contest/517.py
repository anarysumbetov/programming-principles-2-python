import re

a = input()

x = re.findall("\d{2}/\d{2}/\d{4}", a)

print(len(x))