s ={}
print(type(s))
#type is ---> <class 'dict'>
s2 = set()
print(type(s2))
#<class 'set'>

#problem-1

#enter an empty dictionary where 4 people will input there favourite language:
favlang ={}
lan1 = input("enter your favorite language Rubayet: \n")
lan2 = input("enter your favorite language Alam: \n")
lan3 = input("enter your favorite language Bifa: \n")
lan4 = input("enter your favorite language Binoy: \n")
favlang["Rubayet"] = lan1
favlang["Alam"] = lan2
favlang["Bifa"] = lan3
favlang["Binoy"] = lan4
#favlang["Rubayet"] = lan1
#favlang["Rubayet"] = lan2 -----> only this rubayet will be printed 
#favlang["Bifa"] = lan3
#favlang["Binoy"] = lan4
print(favlang)
