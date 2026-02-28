a = input()

class Reverse:
    def __init__(self, string):
        self.string = string

    def process(self):
        return self.string[-1::-1]

r1 = Reverse(a)
print(r1.process())