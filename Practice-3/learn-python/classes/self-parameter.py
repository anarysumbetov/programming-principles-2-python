class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + ". I am " + str(self.age) + " years old.")

p1 = Person("Emil", 25)
p1.greet()

class Person1:
    def __init__(self, name):
        self.name = name
    
    def printName(self):
        print(self.name)

p3 = Person1("Tobias")
p4 = Person1("Linus")

p3.printName()
p4.printName()

class Person2:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)

p5 = Person2("Emil", 36)
p5.greet()

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

class Person3:
    def __init__(self, name):
        self.name = name
     
    def greet(self):
        return "Hello, " + self.name
    
    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website.")

p6 = Person3("Tobias")
p6.welcome()