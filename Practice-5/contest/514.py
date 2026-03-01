import re

a = input()

pattern = re.compile(r"\d+")
result = pattern.fullmatch(a)

if result is not None:
    print("Match")
else:
    print("No match")