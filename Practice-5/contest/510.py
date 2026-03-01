import re

a = input()

x = bool(re.search("cat|dog", a))

if x:
    print("Yes")
else:
    print("No")