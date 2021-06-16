num1 = int(input("enter the 1st number here: "))
num2 = int(input("enter the 2nd number here: "))
num3 = int(input("enter the 3rd number here: "))
num4 = int(input("enter the 4th number here: "))

if (num1>num2):
    big = num1
else:
    big =num2

if (num3>num4):
    big2 = num3
else:
    big2 = num4

if(big>big2):
    print(big,"is the largest number.")
else:
    print(big2,"is the greatest number.")