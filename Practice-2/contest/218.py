a = int(input())
b = []
for i in range(a):
    b.append(input())

c = []
for i in range(a):
    if b[i] not in c:
        c.append(b[i])

c.sort()

for i in range(len(c)):
    print(c[i], (b.index(c[i]) + 1))