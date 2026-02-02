a = int(input())
b = []
for i in range(a):
    b.append(input())

c = []
for i in range(a):
    if b[i] not in c:
        c.append(b[i])

numberCounts = 0
for i in range(len(c)):
    count = b.count(c[i])
    if count == 3:
        numberCounts += 1

print(numberCounts)