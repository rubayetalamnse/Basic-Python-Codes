student1 = int(input("enter your total number in Python: "))
student2 = int(input("enter your total number in Python: "))
student3 = int(input("enter your total number in Python: "))
student4 = int(input("enter your total number in Python: "))
student5 = int(input("enter your total number in Python: "))
student6 = int(input("enter your total number in Python: "))
number_list = [student1,student2,student3,student4,student5,student6]
number_list.sort()
print("All the students numbers are: ",number_list)
result = sum(number_list)
print(result)

#without using only the sum function
print("result is a different way: \n")
result2 =[number_list[0]+number_list[1]+number_list[2]+number_list[3]+number_list[4]+number_list[5]]
print(sum(result2))