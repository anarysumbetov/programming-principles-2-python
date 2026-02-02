a = int(input())
b = []

for i in range(a):
    b.append(input())
c = set(b)
b = list(c)

print(len(b))