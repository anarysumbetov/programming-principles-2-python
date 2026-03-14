a = int(input())
b = list(map(str, input().split()))

for q, w in enumerate(b):
    print(f"{q}:{w}", end=" ")