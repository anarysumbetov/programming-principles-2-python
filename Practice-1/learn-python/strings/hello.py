print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

b = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
print(b)

c = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
print(c)

print(a[1])

for x in "banana":
    print(x)

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")

print("expensive" not in txt)
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")