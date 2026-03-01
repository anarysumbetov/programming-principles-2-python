import math

print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter your name: ")
print(f"Hello {name}")
fav1 = input("What is your favourite animal: ")
fav2 = input("What is your favourite color: ")
fav3 = input("What is your favourite number: ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

x = input("Enter a number: ")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

z = True
while z == True:
    q = input("Enter a really real number: ")
    try:
        q == float(x);
        z = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")