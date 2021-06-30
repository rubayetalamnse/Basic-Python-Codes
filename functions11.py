"""You're planning a vacation, and you need to decide which city you want to visit. You have shortlisted four cities and identified the return flight cost, daily hotel cost, and weekly car rental cost. While renting a car, you need to pay for entire weeks, even if you return the car sooner.

City	Return Flight ($)	Hotel per day ($)	Weekly Car Rental ($)
Paris	      200	              20	                200
London        250	              30	                120
Dubai	      370                 15	                 80
Mumbai	      450	              10	                 70


Answer the following questions using the data above:

1.If you're planning a 1-week long trip, which city should you visit to spend the least amount of money?
2.How does the answer to the previous question change if you change the trip's duration to four days, ten days or two weeks?
3.If your total budget for the trip is $1000, which city should you visit to maximize the duration of your trip? Which city should you visit if you want to minimize the duration?
4.How does the answer to the previous question change if your budget is $600, $2000, or $1500?
Hint: To answer these questions, it will help to define a function cost_of_trip with relevant inputs like flight cost, hotel rate, car rental rate, and duration of the trip. You may find the math.ceil function useful for calculating the total cost of car rental."""
#solve-3----
import math
paris_f,paris_h,paris_c = 200,20,200
london_f,london_h,london_c =250,30,120
dubai_f,dubai_h,dubai_c =370,15,80
mumbai_f,mumbai_h,mumbai_c = 450,10,70

def vacation_cost_trip(flight_cost, hotel_rate,car_rental):
    total_cost = flight_cost  + hotel_rate + car_rental
    return math.ceil(total_cost)

#for 16 days----------------------------------------------------------------
paris_trip = vacation_cost_trip(paris_f,paris_h*16,paris_c*(16/7))
print("to make a 16 days vacation plan in paris, you need to have",paris_trip,"dollars!")

london_trip_expensive = vacation_cost_trip(london_f,london_h*15,london_c*(15/7))
print("to make a 15 days vacation plan in London, you need to have",london_trip_expensive,"dollars!")

dubai_trip = vacation_cost_trip(dubai_f,dubai_h*16,dubai_c*(16/7))
print("to make a 16 days vacation plan in DUBAI, you need to have",dubai_trip,"dollars!")

mumbai_trip = vacation_cost_trip(mumbai_f,mumbai_h*16,mumbai_c*(16/7))
print("to make a 16 days vacation plan in mumbai, you need to have",mumbai_trip,"dollars!")

mumbai_trip_cheap = vacation_cost_trip(mumbai_f,mumbai_h*27,mumbai_c*(27/7))
print("to make 27days vacation plan in mumbai, you need to have",mumbai_trip_cheap,"dollars!")


