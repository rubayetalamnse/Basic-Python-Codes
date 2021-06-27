
class Computer:
    def __init__(self):
        self.name ="Rubayet"
        self.age = 22

    def update(self):
        self.age =30

c1 = Computer()
c2= Computer()

if c1==c2:
    print("Both objects are equal")
