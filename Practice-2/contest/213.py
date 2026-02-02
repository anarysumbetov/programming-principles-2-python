a = int(input())
b = False

for i in range(2, a):
    if a % i == 0:
        b = True

if b:
    print("No")
else:
    print("Yes")