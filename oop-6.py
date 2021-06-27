class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def configure(self): #it's a method
        print("configuration is",self.cpu,self.ram)


com1 = Computer("core i5",8)
com2 = Computer("Ryzen 3",4)
Computer.configure(com1)
Computer.configure(com2)