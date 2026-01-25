age = 36
#This will produce an error:
txt = f"My name is John, I am {age}"
print(txt)

price = 59
hey = f"The price is {price} dollars"
print(hey)

hey = f"The price is {price:.2f} dollars"
print(hey)

hey = f"The price is {20 * 59} dollars"
print(hey)