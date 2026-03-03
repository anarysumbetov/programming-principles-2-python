def func(n):
    return len(n)

x = map(func, "apple", "banana", "cherry")
print(x)

def func2(a, b):
    return a + b

y = map(func2, ("apple", "banana", "cherry"), ("orange", "lemon", "pineapple"))
print(type(y))
print(y)