class Computer:
    def __init__(self):
        self.name ="Rubayet"
        self.age = 22


c1 = Computer()
c2= Computer()
print(id(c1))
print(id(c2))
c2.name = "Yeasa"
c2.age =12
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)