a = ["orange", "mango", "kiwi", "pineapple", "banana"]
a.sort()
print(a)

b = [100, 50, 65, 82, 23]
b.sort()
print(b)

a.sort(reverse = True)
print(a)

b.sort(reverse = True)
print(b)

def myFunc(n):
    return abs(n - 50)

c = [100, 50, 65, 82, 23]
c.sort(key = myFunc)
print(c)

d = ["banana", "Orange", "Kiwi", "cherry"]
d.sort()
print(d)

d.sort(key = str.lower)
print(d)

e = ["banana", "Orange", "Kiwi", "cherry"]
e.reverse()
print(e)