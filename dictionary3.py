mydict = {"name":"Bifa","age":22, "city":"Dhaka"}
print(mydict)

value= mydict["age"]
print(value)

mydict["email"]="rubayetalambifa@gmail.com"
print(mydict)

del mydict["age"]
print(mydict)

try:
    print(mydict["department"])
except :
    print("Error")

for key in mydict:
    print(key)

for i in mydict.keys():
    print(i)

for j in mydict.values():
    print(j)

secondict = mydict.copy()
secondict["email"] = "rubayetalam.nse@gmail.com"
print(secondict)
print(mydict) #original email didn't change

    
dict5 = {"name": "Rubayet","city":"Dhaka"}