import re

a = input()
b = input()

x = bool(re.search(b, a))

if x:
    print("Yes")
else:
    print("No")