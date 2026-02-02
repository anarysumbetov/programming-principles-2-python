myTuple = ("apple", "banana", "cherry")
print(myTuple)
print(len(myTuple))
print(type(myTuple))

duplicateTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(duplicateTuple)

oneItemTuple = ("apple",)
print(type(oneItemTuple))

#NOT a tuple
notATuple = ("apple")
print(type(notATuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple4 = ("abc", 34, True, 40, "male")

tupleMethod = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tupleMethod)