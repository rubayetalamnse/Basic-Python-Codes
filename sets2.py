set1 = {2,3,4,5,6,7,8,9,20}

set2 = {1,3,4,5,6,10,12,18}

set3 = set1.difference(set2)
print(set3)
#Return a set that contains the items that only exist in set1, and not in set2 here the output is {2, 7, 8, 9, 20}
set5 = set2.difference(set1)
print(set5)
#Return a set that contains the items that only exist in set2, and not in set1 here the output is {1, 10, 18, 12}}
set1.difference_update(set2)
print(set1)
#the values which are presented both in set1 and set2 will be removed, and set1 will be printed, here the output is {2, 7, 8, 9, 20}

#intersection mehod----->
set6= set1.intersection(set2)
print("the intersected set is: ",set6)
#only the common elements of both set1 and set2 will be printed in the set4
#