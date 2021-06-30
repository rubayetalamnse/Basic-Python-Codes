"""You're planning a vacation, and you need to decide which city you want to visit. You have shortlisted four cities and identified the return flight cost, daily hotel cost, and weekly car rental cost. While renting a car, you need to pay for entire weeks, even if you return the car sooner.

City	Return Flight ($)	Hotel per day ($)	Weekly Car Rental ($)
Paris	      200	              20	                200
London        250	              30	                120
Dubai	      370                 15	                 80
Mumbai	      450	              10	                 70


Answer the following questions using the data above:

1.If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
2.How does the answer to the previous question change if you change the trip's duration to four days, ten days or two weeks?"""


#solve-2-----------
import math
paris_f,paris_h,paris_c = 200,20,200
london_f,london_h,london_c =250,30,120
dubai_f,dubai_h,dubai_c =370,15,80
mumbai_f,mumbai_h,mumbai_c = 450,10,70



#for 4 days-------
def vacation_cost_4days(flight_cost, hotel_rate,car_rental):
    total_cost = flight_cost  + hotel_rate*4 + car_rental*(4/7)
    return math.ceil(total_cost)


paris_4days = vacation_cost_4days(paris_f,paris_h,paris_c)
print("to make a 4 days vacation plan in paris, you need to have",paris_4days,"dollars!")

london_4days = vacation_cost_4days(london_f,london_h,london_c)
print("to make a 4 days vacation plan in London, you need to have",london_4days,"dollars!")

dubai_4days = vacation_cost_4days(dubai_f,dubai_h,dubai_c)
print("to make a 4 days vacation plan in DUBAI, you need to have",dubai_4days,"dollars!")

mumbai_4days = vacation_cost_4days(mumbai_f,mumbai_h,mumbai_c)
print("to make a 4 days vacation plan in mumbai, you need to have",mumbai_4days,"dollars!")

cheapest_vacation = min([dubai_4days,mumbai_4days,london_4days,paris_4days])
print("the cheapest plan for 4 days vacation is",cheapest_vacation,"dollars!")

import math
paris_f,paris_h,paris_c = 200,20,200
london_f,london_h,london_c =250,30,120
dubai_f,dubai_h,dubai_c =370,15,80
mumbai_f,mumbai_h,mumbai_c = 450,10,70


#for 10 days-------
def vacation_cost_10days(flight_cost, hotel_rate,car_rental):
    total_cost = flight_cost  + hotel_rate*10 + car_rental*(10/7)
    return math.ceil(total_cost)


paris_10days = vacation_cost_10days(paris_f,paris_h,paris_c)
print("to make a 10 days vacation plan in paris, you need to have",paris_10days,"dollars!")

london_10days = vacation_cost_10days(london_f,london_h,london_c)
print("to make a 10 days vacation plan in London, you need to have",london_10days,"dollars!")

dubai_10days = vacation_cost_10days(dubai_f,dubai_h,dubai_c)
print("to make a 10 days vacation plan in DUBAI, you need to have",dubai_10days,"dollars!")

mumbai_10days = vacation_cost_10days(mumbai_f,mumbai_h,mumbai_c)
print("to make a 10 days vacation plan in mumbai, you need to have",mumbai_10days,"dollars!")

cheapest_vacation = min([dubai_10days,mumbai_10days,london_10days,paris_10days])
print("the cheapest plan for 10 days vacation is",cheapest_vacation,"dollars!")

#for-2-weeks------------------------------------------------------------


def vacation_cost_2weeks(flight_cost, hotel_rate,car_rental):
    total_cost = flight_cost  + hotel_rate*14 + car_rental*2
    return math.ceil(total_cost)


paris_2weeks = vacation_cost_2weeks(paris_f,paris_h,paris_c)
print("to make a 2weeks vacation plan in paris, you need to have",paris_2weeks,"dollars!")

london_2weeks = vacation_cost_2weeks(london_f,london_h,london_c)
print("to make a 2weeks vacation plan in London, you need to have",london_2weeks,"dollars!")

dubai_2weeks = vacation_cost_2weeks(dubai_f,dubai_h,dubai_c)
print("to make a 2weeks vacation plan in DUBAI, you need to have",dubai_2weeks,"dollars!")

mumbai_2weeks = vacation_cost_2weeks(mumbai_f,mumbai_h,mumbai_c)
print("to make a 2weeks vacation plan in mumbai, you need to have",mumbai_2weeks,"dollars!")
place_list=[dubai_2weeks,mumbai_2weeks,london_2weeks,paris_2weeks]
cheapest_vacation = min(place_list)
print("the cheapest plan for 2weeks vacation is",cheapest_vacation,"dollars!")

if paris_2weeks == min(place_list):
    print("Lets go to paris for 2weeks")
elif london_2weeks == min(place_list):
    print("Lets go to london for 2weeks")
elif mumbai_2weeks == min(place_list):
    print("Lets go to mumbai for 2weeks")
else:
    print("Lets go to Dubai for 2weeks")
