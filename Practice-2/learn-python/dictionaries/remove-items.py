a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
a.pop("model")
print(a)

a.popitem()
print(a)

b = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del b["model"]
print(b)

del b
#print(b) #this will give an error because "b" no longer exists

c = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
c.clear()
print(c)