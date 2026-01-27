a = int(input())
count = -1

while a != 0:
    if a == 1:
        break
    if a % 2 == 0:
        count+=1
    a = a / 2

if a == 1:
    print("YES")
elif (count != -1) & (a > 0):
    print("YES")
else:
    print("NO")