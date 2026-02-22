def changeCase(func):
    def myInner():
        return func().upper()
    return myInner

@changeCase
def myFunction():
    return "Hello Sally"

print(myFunction())

@changeCase
def otherFunction():
    return "I am speed!"

print(myFunction())
print(otherFunction())

def changeCase2(func):
    def myInner(x):
        return func(x).upper()
    return myInner

@changeCase2
def func1(name):
    return "Hello " + name

print(func1("John"))

def changeCase3(func):
    def myInner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myInner

@changeCase3
def func2(name):
    return "Hello " + name

print(func2("John"))

def changeCase4(n):
    def changeCase4(func):
        def myInner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myInner
    return changeCase4

@changeCase4(1)
def func3():
    return "Hello Linus"

print(func3())

def changeCase5(func):
    def myInner():
        return func().upper()
    return myInner

def addGreeting(func):
    def myInner():
        return "Hello " + func() + " Have a good day!"
    return myInner

@changeCase5
@addGreeting
def func4():
    return "Tobias"

print(func4())

def func5():
    return "Have a nice day!"

print(func5.__name__)

@changeCase
def func6():
    return "Have a great day!"

print(func6.__name__)

import functools

def changeCase6(func):
    @functools.wraps(func)
    def myInner():
        return func().upper()
    return myInner

@changeCase6
def func7():
    return "Have a lovely day!"

print(func7.__name__)