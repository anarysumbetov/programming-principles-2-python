a = int(input())
b = list(map(int, input().split()))

mostFrequent = b[0]
maxCount = 0
for j in range(a):
    theCurrent = b[j]
    count = 0
    i = 0

    while i < a:
        if theCurrent == b[i]:
            count += 1
        if maxCount < count:
            maxCount = count
            mostFrequent = b[i]
        if theCurrent < mostFrequent and count == maxCount:
            mostFrequent = theCurrent
        i += 1

print(mostFrequent)