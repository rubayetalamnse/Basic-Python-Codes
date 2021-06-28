#Use a for loop to display the type of each value stored against each key in person

person = {
    "Name":"Rubayet",
    "Age": 21,
    "HasAndroidPhone": True
}

for i in range(len(person)):
    print(type(person.keys()))
    print(type(person.values()))

for value in person:
    print(type(value))

for key in person:
    print(type(key))
#worked----------------------------------------------------------------
for j in person.values():
    print(type(j))

my_list = ["blue","yellow","green","white",1,True]
my_list.append(30)
print(my_list)
print('My favorite color is', my_list[1])
print('I have {} pet(s).'.format(my_list[4]))

if my_list[5]==True:
    print("I have previous programming experience")
else:
    print("I do not have previous programming experience")

my_list.pop(0)
print("The list has {} elements.".format(len(my_list)))
