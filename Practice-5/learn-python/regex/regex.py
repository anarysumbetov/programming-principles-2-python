import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

y = re.findall("ai", txt)
print(y)

z = re.findall("Portugal", txt)
print(z)

d = re.search("\s", txt)
print("The first white-space character is located in position:", d.start())

e = re.search("Portugal", txt)
print(e)

q = re.split("\s", txt)
print(q)

t = re.split("\s", txt, 1)
print(t)

u = re.sub("\s", "9", txt)
print(u)

o = re.sub("\s", "9", txt, 2)
print(o)

p = re.search("ai", txt)
print(p) # this will print an object

a = re.search(r"\bS\w+", txt)
print(a.span())

s = re.search(r"\bS\w+", txt)
print(s.string)

f = re.search(r"\bS\w+", txt)
print(f.group())