f = open("demofile.txt")
print(f.read())
f.close()

f = open("demofile.txt", "rt") # they are the same
print(f.readline())
f.close()
# f = open("D:\\myfiles\welcome.txt")
# print(f.read())

with open("demofile.txt") as f:
    print(f.read())

with open("demofile.txt") as f:
    print(f.read(5))

with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

with open("demofile.txt", "rt") as f:
    for x in f:
        print(x)