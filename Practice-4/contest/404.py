a, b = list(map(int, input().split()))

def squares(a, b):
    while a <= b:
        yield a * a
        a += 1

res = squares(a, b)
for i in res:
    print(i)