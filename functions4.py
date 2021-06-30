#for home loan-------
""" Radha is planning to buy a house that costs $1,260,000. She considering two options to finance her purchase:

Option 1: Make an immediate down payment of $300,000, and take loan 8-year loan with an interest rate of 10% (compounded monthly) for the remaining amount.
Option 2: Take a 10-year loan with an interest rate of 8% (compounded monthly) for the entire amount."""
import math

def loan_emi(amount):
    emi = amount/12
    print("EMI is $",emi)

loan_emi(126000)
# add a second argument to account for the duration of the loan in months.
def home_loan_emi(amount,duration):
    emi = amount/duration
    print("EMI is $",emi)

home_loan_emi(126000,8*12)
home_loan_emi(126000,10*12)

#with down payment------------------------

def home_emi(amount,duration,down_payment):
    loan_amount = amount-down_payment
    emi = amount/duration
    return emi 

emi1 = home_emi(126000,10*12,300000)
print(emi1)
emi2 = home_emi(126000,8*12,300000)
print(emi2)

#calculating home emi with down payment and interest--------------------

def home_emi_interest(amount,duration,interest,down_payment):
    loan_amount = amount-down_payment
    emi_interest = (loan_amount * interest * ((1+interest) ** duration)) /(((1+interest) **duration)-1)
    return math.ceil(emi_interest)

#emi_interest_8years = home_emi_interest(1260000,96,.1/12,300000)
#
emi_interest_10years = home_emi_interest(1260000,120,.08/12,0)
print("Take a 10-year loan with an interest rate of 8% (compounded monthly) for the entire amount,and EMI :",emi_interest_10years,"$")
#named arguments in function----------------------------------------------------------------
emi_interest_8years = home_emi_interest(amount=1260000, duration =8*12, interest=.1/12, down_payment = 300000)
print("Make an immediate down payment of $300,000, and take loan 8-year loan with an interest rate of 10% (compounded monthly), and EMI :",emi_interest_8years,"$")

if emi_interest_8years < emi_interest_10years:
    print("Option 1 has the lower EMI: ${}".format(emi_interest_8years))
else:
    print("Option 2 has the lower EMI: ${}".format(emi_interest_10years))