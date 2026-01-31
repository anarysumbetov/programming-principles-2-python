a = list(map(int, input().split()))
b = list(map(int, input().split()))

left = a[1]-1
right = a[2]-1

while left < right:
        b[left], b[right] = b[right], b[left] # In-place swap
        left += 1
        right -= 1

for i in range(a[0]):
    print(b[i], end=" ")