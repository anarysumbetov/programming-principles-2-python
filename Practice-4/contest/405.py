a = int(input())

def fun(a):
    while a >= 0:
        yield a
        a -= 1

res = fun(a)
for i in res:
    print(i)