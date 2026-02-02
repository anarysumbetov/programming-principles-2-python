x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "tomato", "pickle")
y = list(x)
y[1] = "potato"
x = tuple(y)

print(x)

q = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "tomato", "pickle")
w = list(q)
w.append("potato")
q = tuple(w)

print(q)

e = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "tomato", "pickle")
r = ("jam",)
e += r
print(e)

t = list(e)
t.remove("apple")
e = tuple(t)

print(e)

del e # this will delte tuple completely