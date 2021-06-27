#we can write less lines by class---------
class Employee:
    def __init__(self,fname,lname,salary): #this is a constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        

rubayet = Employee("Rubayet","Alam",65640)
yeasa = Employee("Yeasin","Al Yeasa",45850)


print(rubayet,yeasa)
print(rubayet.fname,yeasa.fname)