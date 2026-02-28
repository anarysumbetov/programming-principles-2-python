myTuple = ("apple", "banana", "cherry")
myIter = iter(myTuple)

print(next(myIter))
print(next(myIter))
print(next(myIter))

myStr = "qiwi"
myIt = iter(myStr)

print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))

for x in myTuple:
    print(x)

for i in myStr:
    print(i)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myIter1 = iter(myClass)

print(next(myIter1))
print(next(myIter1))
print(next(myIter1))
print(next(myIter1))
print(next(myIter1))

class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass1 = MyNumbers1()
myIter2 = iter(myClass1)

for x in myIter2:
    print(x)