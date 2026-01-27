a = int(input())
b = list(map(int, input().split()))
count = 0

for i in range(a):
    if b[i] > 0:
        count += 1

print(count)