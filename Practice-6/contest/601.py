a = int(input())
b = list(map(int, input().split()))

x = sum(map(lambda i: i ** 2, b))
print(x)