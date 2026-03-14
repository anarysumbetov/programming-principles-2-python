a = int(input())
b = list(map(str, input().split()))

x = max(b, key=len)

print(x)