class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p2 = Person1('Tobias', 28)
print(p2.get_info())

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p3 = Person2("Linus", 25)
p3.celebrate_birthday()
p3.celebrate_birthday()

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p4 = Person3("Emil", 36)
print(p4)

class Person4