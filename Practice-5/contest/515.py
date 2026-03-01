import re

a = input()

def replace(m):
    return m.group(1) + m.group(1)

pattern = re.compile("(\d)")
result = pattern.sub(replace, a)

print(result)