with open("demofile-2.txt", "a") as f:
    f.write("Now the file has more content!")

# open and read the file after the appending
with open("demofile-2.txt") as f:
    print(f.read())

with open("demofile-2.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

# open and read the file after the overwriting:
with open("demofile-2.txt") as f:
    print(f.read())

f = open("myfile.txt", "x")