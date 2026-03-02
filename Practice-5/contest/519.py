import re

a = input()

pattern = re.compile("\w+")
result = re.findall(pattern, a)

print(len(result))