a = input()

# for i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
#     print(i in a)

x = any(i in a for i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

if x:
    print("Yes")
else:
    print("No")