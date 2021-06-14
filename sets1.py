a ={1,3,1,4,5}
print(a)
print(type(a))
#sets don't allow duplicate elements, so output is--{1,3,4,5}
b= set()
print(type(b))
print(b)
#adding elements in the set b--->
b.add(5)
b.add(10)
b.add(15)
print(b)
#we can't add any list/dictionary in a set
#we can add tuple in a set
b.add((2,3,4))
print(b)
#can't use index
b.remove(15)
print(b)
#we can't remove any element which is not even avilable in the set
print(b.pop())
#it removes the last values we have inserted in the set,
#we inserted a tuple lastly which was ---> (2,3,4)