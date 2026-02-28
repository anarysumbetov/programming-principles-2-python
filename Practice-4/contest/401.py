a = int(input())

def f(max):
    count = 1
    while count <= max:
        yield count * count
        count += 1

countRange = f(a)
for n in countRange:
    print(n)