list1 = [False, True, False]
x = any(list1)
print(x)

tuple1 = (0, 1, False)
y = any(tuple1)
print(y)

set1 = {0, 1, 0}
z = any(set1)
print(z)

dict1 = {0: "Apple", 1: "Orange"}
d = any(dict1)
print(d)