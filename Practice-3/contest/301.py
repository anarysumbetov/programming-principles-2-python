def check():
    global hey, a
    while a > 0:
        b = a % 10
        if b % 2 == 0:
            hey = True
        else:
            hey = False
            break
        a = a // 10

a = int(input())
hey = False
check()

if hey:
    print("Valid")
else:
    print("Not valid")