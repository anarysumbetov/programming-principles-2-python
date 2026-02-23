x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

def func1(n):
    return lambda a : a * n

print(func1(4))

doubler = func1(2)
print(doubler(11))

tripler = func1(3)
print(tripler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numeros = list(filter(lambda x : x % 2 != 0, numeros))
print(odd_numeros)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key = lambda x : x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key = lambda x : len(x))
print(sorted_words)