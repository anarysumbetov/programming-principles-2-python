fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print(fruits)

a = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = a

print(green)
print(yellow)
print(red)
print(a)

b = ("apple", "mango", "papaya", "pineapple", "banana", "cherry")

(green, *tropic, red) = b

print(green)
print(tropic)
print(red)
print(b)