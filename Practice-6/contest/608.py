a = int(input())
b = list(map(int, input().split()))

x = sorted(set(b))

for i in x:
    print(i, end = " ")