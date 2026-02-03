a = int(input())
b = {}

for i in range(a):
    c = input().split()
    if c[0] in b:
        b[c[0]] = str(int(b[c[0]]) + int(c[1]))
    else:
        b[c[0]] = c[1]

q = list(b)
q.sort()

for i in q:
    print(i, b.get(i))