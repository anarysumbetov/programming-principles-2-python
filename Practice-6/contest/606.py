a = int(input())
b = list(map(int, input().split()))

x = all(i > -1 for i in b)

if x:
    print("Yes")
else:
    print("No")