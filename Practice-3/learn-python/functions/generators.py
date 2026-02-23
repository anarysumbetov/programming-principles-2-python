def gen1():
    yield 1
    yield 2
    yield 3

for value in gen1():
    print(value)

def countUpTo(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in countUpTo(5):
    print(num)

def largeSequence(n):
    for i in range(n):
        yield i

# This does not create a million numbers in memory
gen = largeSequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

def simpleGen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"

gen = simpleGen()
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) # Stop iteration exception

list_comprehension = [x * x for x in range(5)]
print(list_comprehension)

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

total = sum(x * x for x in range(10))
print(total)

def fibbonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen2 = fibbonacci()
for _ in range(100):
    print(next(gen2))

def echo_generator():
    while True:
        received = yield
        print("Received:", received)

gen3 = echo_generator()
next(gen3)
gen3.send("Hello")
gen3.send("World")

def gen4():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen5 = gen4()
print(next(gen5))
gen5.close()