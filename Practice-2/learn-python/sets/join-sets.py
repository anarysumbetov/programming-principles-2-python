set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)


set5 = {"John", "Elena"}
set6 = {"apple", "bananas", "cherry"}

combo = set1.union(set2, set5, set6)
print(combo)

comboUltra = set1 | set2 | set5 | set6
print(comboUltra)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

x.update(y)
print(x)

r = {"apple", "banana", "cherry"}
t = {"google", "microsoft", "apple"}

o = r.intersection(t)
print(o)
p = r & t
print(p)

r.intersection_update(t)
print(r)

duplicate1 = {"apple", 1, "banana", 0, "cherry"}
duplicate2 = {False, "google", 1, "apple", 2, True}

duplicate3 = duplicate1.intersection(duplicate2)
print(duplicate3)

duplicate4 = duplicate1.difference(duplicate2)
print(duplicate4)

duplicate5 = duplicate1 - duplicate2
print(duplicate5)

duplicate1.difference_update(duplicate2)
print(duplicate1)

duplicate6 = duplicate1.symmetric_difference(duplicate2)
print(duplicate6)

duplicate7 = duplicate1 ^ duplicate2
print(duplicate7)

duplicate1.symmetric_difference_update(duplicate2)
print(duplicate1)