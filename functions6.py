#If you borrow $100,000 using a 10-year loan with an interest rate of 9% per annum, what is the total amount you end up paying as interest?

import math
#for loan emi------------------------
loan = 100000
loan_duration = 10*12 #10 years
interest_rate = .09/12 #compounded monthly


#reusing our previous function to calculate emi---------
def loan_emi_interest(amount,duration,interest,down_payment):
    loan_amount = amount-down_payment
    try:
        emi_interest = (loan_amount * interest * ((1+interest) ** duration)) /(((1+interest) **duration)-1)
    except ZeroDivisionError:
        emi_interest = loan_amount/duration
    return math.ceil(emi_interest)

#calling our function to calculate emi with interest------------
emi_with_interest =loan_emi_interest(amount = loan, duration =loan_duration, interest=interest_rate, down_payment=0)
print("EMI WITH Interest:",emi_with_interest)

#calling our function to calculate emi without interest------------
emi_without_interest =loan_emi_interest(amount = loan, duration =loan_duration, interest=0, down_payment=0)
print("EMI without Interest:",emi_without_interest)

#total interest-------
total_interest = emi_with_interest - emi_without_interest
print("total interest per month:",total_interest)
print("total interest for 10 year:",total_interest*120)