thisIsDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisIsDict)
print(thisIsDict["brand"])

duplicateDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(duplicateDict)
print(len(duplicateDict))

anyDict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colours": ["red", "white", "blue"]
}
print(type(anyDict))

kchau = dict(name = "John", age = 36, country = "Norway")
print(kchau)