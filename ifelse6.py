payment = float(input("enter your total payment: "))
#if(payment>500 or payment<1000):
if(payment>500 and payment<10000):
    print("you can pay via card or Bkash. ")
else:
    print("please give us cash.")
#any amount will bring for "or" ----->you can pay via card or Bkash.
#any amount less than 501 will bring for "and" ----->please give us cash.
##any amount more than 500 will bring for "and" ----->you can pay via card or Bkash.