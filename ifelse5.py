age = int(input("enter your age: "))
if (age>20 and age<35):
    print("you can work in team A!")
else:
    print("Please join team B")

payment = float(input("enter your total payment: "))
if(payment>500.0 or payment<1000.0):
    print("please give us cash. ")
else:
    print("you can pay via card or Bkash.")