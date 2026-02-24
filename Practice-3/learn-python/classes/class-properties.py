class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person1("Tobias", 25)
print(p2.age)

p2.age = 26
print(p2.age)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p3 = Person2("Linus", 30)

del p3.age

print(p3.name) # This works
# print(p3.age) # This would cause an error

class Person3:
    species = "Human" # Class property

    def __init__(self, name):
        self.name = name # Instance property

p4 = Person3("Emil")
p5 = Person3("Tobias")

print(p4.name)
print(p5.name)
print(p4.species)
print(p5.species)

class Person4:
    lastName = ""

    def __init__(self, name):
        self.name = name

p6 = Person4("Linus")
p7 = Person4("Emil")

Person4.lastName = "Refsnes"

print(p6.lastName)
print(p7.lastName)

class Person5:
    def __init__(self, name):
        self.name = name

p8 = Person5("Tobias")

p8.age = 25
p8.city = "Oslo"

print(p8.name)
print(p8.age)
print(p8.city)