# Python program to calculate the sum of n Natural Numbers using while loop
num = int(input("enter any number: "))
natural_number = num
sum = 0
if num<0:
    print("please enter a positive number: ")
else:
    while num>0:
        sum = sum+num
        num = num-1
    print("sum of first",natural_number, "number is =",sum)