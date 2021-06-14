tuple1 = (1,5,10,20,50)
print(tuple1)
tuple2 = (100,) #single element tuple
print(tuple2)
#tuple1[0] = 2 we can't change any tuple!

tuple3 = (2,4,8,12,16,20,40,2,4,60,64,2,80,84,88,92,2,96,100,2)
print(tuple3.count(2))
print(len(tuple3))
print(tuple3.index(88))
nested_tuple = tuple1,tuple3,("ruba","alam","binu","alam")
print(nested_tuple)
print(len(nested_tuple))
print(type(nested_tuple))
empty_tuple = ()
print(empty_tuple)
print(len(empty_tuple))
