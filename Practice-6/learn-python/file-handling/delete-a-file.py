import os
if os.path.exists("demofile-3.txt"):
    os.remove("demofile-3.txt")
else:
    print("The file does not exist")

# os.rmdir("myfolder")