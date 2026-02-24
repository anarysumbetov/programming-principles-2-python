class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

class Person1:
    pass

p2 = Person1()
p2.name = "Tobias"
p2.age = 25

print(p2.name)
print(p2.age)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p3 = Person2("Linus", 28)

print(p3.name)
print(p3.age)

class Person3:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p4 = Person3("Emil")
p5 = Person3("Tobias", 25)


print(p4.name, p4.age)
print(p5.name, p5.age)

class Person4:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p6 = Person4("Linus", 30, "Oslo", "Norway")

print(p6.name)
print(p6.age)
print(p6.city)
print(p6.country)