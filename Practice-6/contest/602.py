a = int(input())
b = list(map(int, input().split()))

x = len(list(filter(lambda i: i % 2 == 0, b)))

print(x)