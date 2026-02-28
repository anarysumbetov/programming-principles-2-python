txt = f"The price is 49 dollars"
print(txt)

price = 49
txt1 = f"The price is {price} dollars"
print(txt1)

price2 = 59
txt2 = f"The price is {price2:.2f} dollars"
print(txt2)

txt3 = f"The price is {95:.3f} dollars"
print(txt3)

txt4 = f"The price is {20 * 59} dollars"
print(txt4)

price3 = 32
tax = 0.25
txt5 = f'The price is {price3 + (price3 * tax)} dollars'
print(txt5)

price4 = 29
txt6 = f"It is very {"Expensive" if price4 > 50 else "Cheap"}"

print(txt6)

fruit = "apples"
txt7 = f"I love {fruit.upper()}"
print(txt7)

def converter(x):
    return x * 0.3048

txt8 = f"The plane is flying at a {converter(30000)} meter altitude"
print(txt8)

price5 = 59000
txt9 = f"The price is {price5:,} dollars"
print(txt9)

price6 = 23
txt10 = "The price is {} dollars"
print(txt10.format(price6))

txt11 = "The price is {:.2f} dollars"
print(txt11.format(price6))

quantity = 3
itemNo = 567
price7 = 2309
myOrder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myOrder.format(quantity, itemNo, price7))

myOrder = "I want {2} pieces of item number {1} for {0:.2f} dollars."
print(myOrder.format(quantity, itemNo, price7))

age = 36
name = "John"
txt12 = "His name is {1}. {1} is {0} years old."
print(txt12.format(age, name))

myOrder1 = "I have a {carName}, it is a {model}."
print(myOrder1.format(carName = "Ford", model = "Mustang"))
