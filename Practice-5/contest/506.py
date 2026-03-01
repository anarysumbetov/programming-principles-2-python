import re

a = input()

x = re.search(r"\s*\S+@\S+\.\S+\s*", a)

if x is not None:
    print(x[0].strip())
else:
    print("No email")