a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = b[a[1]-1: a[2]]

for i in range(len(c)):
    b.pop(a[1]-1)

for i in range(len(c)):
    b.insert(a[1]-1, c[i])

for i in range(len(b)):
    print(b[i], end=" ")