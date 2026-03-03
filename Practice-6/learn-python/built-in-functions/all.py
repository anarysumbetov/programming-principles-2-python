list1 = [True, True, True]
x = all(list1)
print(x)

list2 = [0, 1, 1]
y = all(list2)
print(y)

tuple1 = (0, True, False)
z = all(tuple1)
print(z)

set1 = {0, 1, 0}
q = all(set1)
print(q)

dict1 = {0: "Apple", 1: "Orange"}
w = all(dict1)
print(w)