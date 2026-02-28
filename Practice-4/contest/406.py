a = int(input())

def fibonacci():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, second + first

gen = fibonacci()
for i in range(a):
    if i != 0:
        print(",", end="")
    print(next(gen), end="")
