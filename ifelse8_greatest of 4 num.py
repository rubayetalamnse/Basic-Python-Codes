num1 = int(input("enter the 1st number here: "))
num2 = int(input("enter the 2nd number here: "))
num3 = int(input("enter the 3rd number here: "))
num4 = int(input("enter the 4th number here: "))
if (num1>num2 and num1>num3 and num1>num4):
    print(num1, "is the greates number.")
elif (num2>num1 and num2>num3 and num2>num4):
    print(num2, "is the greatest number.")
elif (num3>num1 and num3>num2 and num3>num4):
    print(num3, "is the greatest number.") 
else:
    print(num4, "is the greatest number")  