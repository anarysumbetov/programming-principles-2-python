import re

a = input()

x = bool(re.match("Hello", a))

if x:
    print("Yes")
else:
    print("No")