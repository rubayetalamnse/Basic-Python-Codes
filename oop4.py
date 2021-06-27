#before creating a fan we have to design it in Solidworks.
#design = class(), fan=object/Instance
#a class has 2 things: attributes and methods
#attributes = are mainly variables,for a fan- color, number of blades, price, size are attributes.
#methods are functions, they define the behavior of the class. like a fan will move at 300/350 RPM,220-240v

class Computer:
    def configure(self): #it's a method
        print("i5, 8th-gen, 1TB, 8gb-Ram, 15.6-inches")

#let's create an object for the class - "computer"
com1 = Computer()
com2 = Computer()
print(type(com1))

#there are inbuild classes in python, such as str,int,float, etc.
#we have to mention the classes we have built before calling the function
Computer.configure(com1)
Computer.configure(com2)
#or we have to specify the objects within the function
com1.configure()
com2.configure() 
#here the configure function will take the com1 as a parameter and will pass them at self.

