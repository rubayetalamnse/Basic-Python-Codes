passage1 = "This is an example of double  space"
print(passage1.find("  "))
#we will get 28---> which is the index number of the double space

passage2= "Nuclear Power is good for all of us."
print(passage2.find("  "))
#the output is--->-1, because there is no double spae available.

#now we will remove the double spaces from passage1
print(passage1.replace("  "," "))
#output: This is an example of double space
letter= "Dear Harry,\n\tThank you for providing a free python course!\n\tYou can also make a series on machine learning or data science\n\tYours Students"