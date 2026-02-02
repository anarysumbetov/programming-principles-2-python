a = ["apple", "banana", "cherry"]
for i in a:
    print(i)

for j in range(len(a)):
    print(a[j])

k = 0
while k < len(a):
    print(a[k])
    k = k + 1

[print(x) for x in a]