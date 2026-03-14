a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# s = 0

# for i in range(a):
#     s = s + b[i] * c[i]

# print(s)

s = 0

for q, w in zip(b, c):
    s = s + q * w

print(s)