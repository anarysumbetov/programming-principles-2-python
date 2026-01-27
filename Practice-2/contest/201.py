a = int(input())

if a % 4 == 0 & (a / 100 != a // 100):
    print("YES")
elif a % 400 == 0  & (a / 100 != a // 100):
    print("YES")
else:
    print("NO")