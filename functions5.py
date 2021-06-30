#Shaun is currently paying back a home loan for a house he bought a few years ago. The cost of the house was $800,000. Shaun made a down payment of 25% of the price. He financed the remaining amount using a 6-year loan with an interest rate of 7% per annum (compounded monthly). Shaun is now buying a car worth $60,000, which he is planning to finance using a 1-year loan with an interest rate of 12% per annum. Both loans are paid back in EMIs. What is the total monthly payment Shaun makes towards loan repayment?

import math

#for house emi------------------------
cost_of_house = 800000
down_payment_house = .25*cost_of_house
loan_duration_house = 6*12 #6 years
interest_rate_house = .07/12 #compounded monthly

#for car emi------------------------
cost_of_car = 60000
loan_duration_car = 12
interest_rate_car = .12/12
down_payment_car = 0


#reusing our previous function---------
def loan_emi_interest(amount,duration,interest,down_payment):
    loan_amount = amount-down_payment
    emi_interest = (loan_amount * interest * ((1+interest) ** duration)) /(((1+interest) **duration)-1)
    return math.ceil(emi_interest)


#calling our function for calculating house emi------------------------

house_emi =loan_emi_interest(amount=cost_of_house, duration=loan_duration_house, interest=interest_rate_house, down_payment=down_payment_house)

print("The house emi is now {}".format(house_emi))


#calling our function for calculating car emi------------------------
car_emi =loan_emi_interest(amount=cost_of_car, duration=loan_duration_car, interest=interest_rate_car, down_payment=down_payment_car)

print("The house emi is now {}".format(car_emi))

#total emi------------------------
total_emi = house_emi + car_emi
print("\n Shaun had to pay per month",total_emi,"Dollars for both house and car EMIs.")
