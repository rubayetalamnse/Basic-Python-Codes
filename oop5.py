class Computer:
    def __init__(self):
        print("init")

    def configure(self): #it's a method
        print("i5, 8th-gen, 1TB, 8gb-Ram, 15.6-inches")


com1 = Computer()
com2 = Computer()
Computer.configure(com1)
Computer.configure(com2)
#init will be printed 2 times because of com1 and com2