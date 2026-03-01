import re

s = input()
d = input()

x = re.split(d, s)

for i in range(len(x)):
    if i != 0:
        print("", end=",")
    print(x[i], end="")