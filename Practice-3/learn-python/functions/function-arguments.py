def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def func2(name): # name is parameter
    print("Hello", name)

func2("Emil") # "Emil" is an argument

def func3(fname, lname):
    print(fname + " " + lname)

func3("Emil", "Refsnes")

#func3("Emil") # you will get an error

def kchau(name = "friend"):
    print("Hello", name)

kchau("Emil")
kchau("Tobias")
kchau()
kchau("Linus")

def dec(country = "Norway"):
    print("I am from", country)

dec("Sweden")
dec("India")
dec()
dec("Brazil")

def animalName(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

animalName(animal = "dog", name = "Buddy")
animalName(name = "Buddy", animal = "dog")
animalName("dog", "Buddy")
animalName("Buddy", "dog")

def animalNameAge(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

animalNameAge("dog", name = "Buddy", age = 5)

def smth1(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
smth1(my_fruits)

def dict(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
dict(my_person)

def math1(x, y):
    return x + y

result = math1(5, 3)
print(result)

def smth2():
    return ["apple", "banana", "cherry"]

fruits2 = smth2()
print(fruits2[0])
print(fruits2[1])
print(fruits2[2])

def smth3():
    return (10, 20)

x, y = smth3()
print("x:", x)
print("y:", y)

def smth4(name, /):
    print("Hello", name)

smth4("Emil")

def smth5(name):
    print("Hello", name)

smth5(name = "Emil")

"""
def smth6(name, /):
    print("Hello", name)

smth6(name = "Emil") # you will get an error
"""

def smth7(*, name):
    print("Hello", name)

smth7(name = "Emil")

def smth8(name):
    print("Hello", name)

smth8("Emil")

"""
def smth9(*, name):
    print("Hello", name)

smth9("Emil") # you will get an error
"""

def smth10(a, b, /, *, c, d):
    return a + b + c + d

result2 = smth10(5, 10, c = 15, d = 20)
print(result2)