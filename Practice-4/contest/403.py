a = int(input())

def func(max):
    cnt = 0
    while cnt <= max:
        if cnt % 3 == 0 and cnt % 4 == 0:
            yield cnt
        cnt += 1

ctr = func(a)
for n in ctr:
    print(n, end=" ")