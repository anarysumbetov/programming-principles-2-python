i = 1
while i < 6:
    print(i, end=" ")
    i += 1
print()

j = 1
while j < 6:
    print(j, end=" ")
    if j == 3:
        break
    j += 1
print()

k = 0
while k < 6:
    k += 1
    if k == 3:
        continue
    print(k, end=" ")
print()

h = 1
while h < 6:
    print(h, end=" ")
    h += 1
else:
    print("h is no longer less than 6")