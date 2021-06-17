# Python program to calculate the sum of n Natural Numbers using for loop
num = int(input("enter any number: "))

sum = 0
if num<0:
    print("please enter a positive number: ")
else:
    for num in range (1,num+1,1):
        sum = sum+num
        print("Sum of first", num, "numbers is: ", sum)
        average = sum/num
        print("Average of first", num, "numbers is: ", average)
