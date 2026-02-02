a = int(input())
b = list(map(int, input().split()))
c = []
for i in range(a):
    if b[i] not in c:
        print("YES")   
        c.append(b[i]) 
    else:
        print("NO")
        c.append(b[i])