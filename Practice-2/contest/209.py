a = int(input())
b = list(map(int, input().split()))
max = b[0]
min = b[0]

for i in range(a):
    if max < b[i]:
        max = b[i]
    if min > b[i]:
        min = b[i]

for j in range(a):
    if b[j] == max:
        b[j] = min

for k in range(a):
    print(b[k], end=" ")