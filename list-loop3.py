list1 = [2,3,4,5,6,7]
for x in list1:
    if(x%2==1 and x>4):
        print(x)
        break

list2 = list(range(3,15,3))
print(list2[2])

list3 = [1,1,2,3,5,8,13]
print(list3[list3[4]])

""" Print the first element of the list, if it contains even number of elements or Print first element if length of the list is even.""" 
list5 =[1,2,3,4]
if len(list5)%2==0:
    print(list5[0])