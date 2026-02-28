class Person:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName

    def printName(self):
        print(self.firstName, self.lastName)

#Use the Person class to create an object, and then execute the printName method:

x = Person("John", "Doe")
x.printName()

class Student(Person):
    def __init__(self, fName, lName, year):
        super().__init__(fName, lName)
        self.graduationYear = year

    def welcome(self):
        print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationYear)

x = Student("Mike", "Olsen", 2019)
x.printName()
x.welcome()