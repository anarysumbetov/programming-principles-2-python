fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)

c = [x for x in fruits if "b" in x]
print(c)

d = [x for x in fruits if x != "apple"]
print(d)

e = [x for x in fruits]
print(e)

f = [x for x in range(10)]
print(f)

g = [x for x in range(10) if x < 5]
print(g)

h = [x.upper() for x in fruits]
print(h)

i = ["hello" for x in fruits]
print(i)

j = [x if x != "banana" else "orange" for x in fruits]
print(j)