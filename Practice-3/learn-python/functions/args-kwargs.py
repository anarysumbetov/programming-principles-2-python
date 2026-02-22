def func1(*kids):
    print("The youngest child is " + kids[2])

func1("Emil", "Tobias", "Linus")

def func2(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

func2("Emil", "Tobias", "Linus")

def func3(greeting, *names):
    for name in names:
        print(greeting, name)

func3("Hello", "Emil", "Tobias", "Linus")

def func4(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(func4(1, 2, 3))
print(func4(10, 20, 30, 40))
print(func4(5))

def func5(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(func5(3, 7, 2, 9, 1))

def func6(**kid):
    print("His las name is " + kid["lname"])

func6(fname = "Tobias", lname = "Refsnes")

def func7(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

func7(name = "Tobias", age = 30, city = "Bergen")

def func8(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

func8("emil123", age = 25, city = "Oslo", hobby = "coding")

def func9(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

func9("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def func10(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = func10(*numbers) # Same as: func10(1, 2, 3)
print(result) 

def func11(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
func11(**person) # Same as: func11(fname = "Emil", lname = "Refsnes")