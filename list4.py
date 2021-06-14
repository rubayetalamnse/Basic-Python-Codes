nums = [0, 1, 2, 45, 67, 9]
print(nums[0])
nums[0] = 25
print(nums[-1])
print(nums)
# we can access different elements by using their index number
# now the list is -[25,1,2,45,67,9]
# index 0-->nums[0]--->25
# index 1-->nums[1]--->1
# index 2-->nums[2]--->2
# index -1-->last elements of a list--->9
list1 = [24, 56.78, 90, 500, "samsung", "walton"]
print(list1[0:4])
print(list1[-1])
str1 = "Rubayet"
print(str1[0:4])
print(str1[4:])
print(str1[-1])
print(str1.index('a'))  # index number of 'a' in rubayet is 3.
str2 = str1[0:str1.index('a')]
print(str2)
str3 = str1[str1.index('a')+1:]
print(str3)
strrr = "alam"
str4 = strrr[strrr.index('a')+1:]
print(str4)
str5 = "  bifa  "
print(str5.strip())
print(str1[2:5])
name = "Rubayet, Alam"
# we can do the same thing with string and list
para = "Nuclear is the best     energy option before all of us! "
print(para.strip())
print(para.upper())
print(para.lower())
print(name.split(" ,"))
