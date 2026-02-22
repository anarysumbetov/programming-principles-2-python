def func1():
    x = 300
    print(x)

func1()

def func2():
    x = 200
    def func3():
        print(x)
    func3()

func2()

x = 100

def func4():
    print(x)

func4()

print(x)

y = 400

def func5():
    y = 500
    print(y)

func5()
print(y)

def func5():
    global z
    z = 123

func5()
print(z)

r = 123134

def func6():
    global r
    r = 987907

func6()
print(r)

def func6():
    x = "Jane"
    def func7():
        nonlocal x
        x = "hello"
    func7()
    return x

print(func6())

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)