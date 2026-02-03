a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = a["model"]
print(x)
y = a.get("model")
print(y)

z = a.keys()
print(z)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

q = car.keys()

print(q) # before the change

car["color"] = "white"

print(q) # after the change

h = car.items()
print(h)
w = car.values()

print(w) # before the change

car["year"] = 2020
car["color"] = "red"

print(w) # after the change
print(h)

if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")