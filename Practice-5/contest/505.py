import re

a = input()

x = bool(re.findall(r"^[a-zA-Z].*[0-9]$", a))

if x:
    print("Yes")
else:
    print("No")