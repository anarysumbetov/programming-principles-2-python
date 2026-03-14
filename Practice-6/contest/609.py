a = int(input())
b = list(map(str, input().split()))
c = list(map(str, input().split()))
d = input()

l = {}

for q, w in zip(b, c):
    l[q] = w

if d in l:
    if type(l[d]) == int:
        print(int(l[d]))
    else:
        print(l[d])
else:
    print("Not found")