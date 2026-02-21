fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for i in "banana":
    print(i)

for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        break
    print(x)

for x in fruits:
    if x == "banana":
        continue
    print(x)

for i in range(6):
    print(i, end=" ")
print()

for j in range(2, 6):
    print(j, end=" ")
print()

for k in range(2, 30, 3):
    print(k, end=" ")
print()

for v in range(6):
    print(v, end=" ")
else:
    print("Finally finished!")

for v in range(6):
    if v == 3: break
    print(v, end=" ")
else:
    print("Finally finished!")
print()

adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass