mytuple = tuple(["banana","cherry","mango","apple"])
print(mytuple)
print(type(mytuple))
tuple2 = ("Dhaka",)
print(type(tuple2))

letters = ('a','p','p','l','e')
print(letters.index('p'))
print(letters.index('p'))

details = "Rubayet", 201828008, "NSE"
name,ID, department = details
print(name)
print(ID)
print(department)

numbers = (1,2,3,4,5,6)
i1, *i2,i3 = numbers
print(i1)
print(i2)
print(i3)


import sys
my_list = [0,1,2,"Rubayet",True]
my_tuples =(0,1,2,"Rubayet",True)
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuples),"bytes")

import timeit
print(timeit.timeit(stmt="[1,2,3,4,5,6]",number =10000))
print(timeit.timeit(stmt="(1,2,3,4,5,6)",number =10000))
