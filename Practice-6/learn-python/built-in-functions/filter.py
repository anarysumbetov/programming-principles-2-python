ages = [5, 12, 17, 18, 24, 32]

def func1(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(func1, ages)

for i in adults:
    print(i)