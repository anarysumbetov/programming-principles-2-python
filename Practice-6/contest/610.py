a = int(input())
b = list(map(int, input().split()))

x = sum(map(lambda i: i != 0, b))

print(x)