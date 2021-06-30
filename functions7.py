#Robert is currently paying back a home loan for a house he bought a few years ago. The cost of the house was 1250000. Shaun made a down payment of 800000 of the price. He financed the remaining amount using a 14-year loan with an interest rate of 10% per annum (compounded monthly) for first 4 years (2015-2018). And interest rate became 9.90% for the last 3 years(2019-2021).loan is paid back in EMIs. What is the total monthly payment Robert makes towards loan repayment?

import math

cost_of_house = 1250000
duration_of_house = 4*12 #2015,2016,2017,2018
down_payment_house = 800000
interest_rate_4yrs = .10/12

#reusing our previous function---------
def loan_emi_interest(amount,duration,interest,down_payment):
    loan_amount = amount-down_payment
    emi_interest = (loan_amount * interest * ((1+interest) ** duration)) /(((1+interest) **duration)-1)
    return math.ceil(emi_interest)

#calling our function for calculating house emi(2015-2018)-------------------

house_emi_4yrs =loan_emi_interest(amount=cost_of_house, duration=duration_of_house, interest=interest_rate_4yrs, down_payment=down_payment_house)

print("The house emi is for(2015-2018) at 12%/month interest rate: {}".format(house_emi_4yrs))

total_4 =house_emi_4yrs*48
print("total emi for 4 years:",total_4)

#calling our function for calculating house emi(2019-2021)-------------------
cost_of_house = 1250000
duration_of_house = 3*12 #2019,2020,2021
down_payment_house = 800000+590256
interest_rate_4yrs = .099/12

house_emi_3yrs =loan_emi_interest(amount=cost_of_house, duration=duration_of_house, interest=interest_rate_4yrs, down_payment=down_payment_house)

print("The house emi is for(2019-2021) at 9.90%/month interest rate: {}".format(abs(house_emi_3yrs)))

total_3 =abs(house_emi_3yrs*36)
print("total emi for 3 years(2019-2021):",abs(total_3))

total_7 = total_3 +total_4
print("Total paid in last 7 years(2015-2021):",total_7+800000)