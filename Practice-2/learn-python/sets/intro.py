mySet = {"apple", "banana", "cherry"}

thisIsSet = {"apple", "banana", "cherry"}
print(thisIsSet)

a = {"apple", "banana", "cherry", "apple", "melon"}
print(a)

b = {"apple", "banana", "cherry", True, 1, 2} # True and 1 are the same values
print(b)

c = {"apple", "banana", "cherry", False, 0, True} # False and 0 are the same values
print(c)

d = {"apple", "banana", "cherry"}
print(len(d))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set4 = {"abc", 34, True, 40, "male"}
print(type(set4))

set5 = {1}
print(set5)
print(type(set5))

set6 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(set6)