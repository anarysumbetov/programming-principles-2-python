a = int(input())

for i in range(2, 6):
    if(a / i == a // i):
        a = a / i
        
if (a / 1 == a // 1) and a == 1:
    print("Yes")
else:
    print("No")