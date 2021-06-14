set1 = {2,3,4,5,6,7,8,9,20}

set2 = {1,3,4,5,6,10,12,18}

#intersection mehod----->
set6= set1.intersection(set2)
print("the intersected set is: ",set6)
#only the common elements of both set1 and set2 will be printed in the set4
#the intersected set is:  {3, 4, 5, 6}

#intersection_update mehod----->
set1.intersection_update(set2)
print(set1)
#Remove the items that is not present in both set1 and set2:
#output:----->{3, 4, 5, 6}

#issubset method------>
a_set = {3,4,5,10}
b_set = {1,2,3,4,5,10,20,50}
new_set = a_set.issubset(b_set)
print(new_set)
#Return True if all items in a_set are present in b_set

#issuperset method----->
super_set = a_set.issuperset(b_set)
print(super_set)
#Return True if all items b_set are present in a_set:---we get FALSE

#union method---->
union_set = a_set.union(b_set)
print(union_set)
#Return a set that contains all items from both sets, duplicates are excluded
#output---->{1, 2, 3, 4, 5, 10, 50, 20}

#update method---->
c_set ={9,11,13,17,23,59}
b_set.update(c_set)
print(b_set)
#Insert the items from c_set into set b_set:
#output---> {1, 2, 3, 4, 5, 9, 10, 11, 13, 17, 50, 20, 23, 59}

