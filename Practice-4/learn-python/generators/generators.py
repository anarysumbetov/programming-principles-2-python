def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt +=1

ctr = fun(5)
for n in ctr:
    print(n)

def fun1():
    yield 1
    yield 2
    yield 3

for val in fun1():
    print(val)

def fun2():
    return 1 + 2 + 3

res = fun2()
print(res)

sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)