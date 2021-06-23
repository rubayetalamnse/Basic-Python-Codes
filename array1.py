from array import *

#lets put everyone's marks in an array
values =  array("i",[10,-20,30,40,50])
print(values)

#cloning our first array--values

clone_values = array(values.typecode,(a for a in values))
print("Printing our cloned array: ")
for i in clone_values:
    print(i)



#another array------------------------
values2 = array("i",[5,9,-8,4,-2])
values2.reverse()
print(values2)
print(values2.buffer_info())
#output--->(2804324346384 ==address, 5==total elements of the array)
 
#we can use indexing in array
print(values[0]) #fist element is 5

#for i in range(len(values)): -----or--
for i in range(5):
    print(values[i])

char_array = array('u',['r','a','t','s'])
#print(char_array)
for character in char_array:
    print(character)