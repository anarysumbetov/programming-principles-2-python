a = 5
b = 2
if a > b: print("a is greater than b")

c = 2
d = 330
print("A") if c > d else print("B")

e = 10
f = 20
bigger = e if e > f else f
print("Bigger is", bigger)

g = 330
h = 330
print("A") if g > h else print("=") if g == h else print("B")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)