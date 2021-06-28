#Q11b (Optional): Out of the 29 people who took the flight, only 12 buy tickets to return from the Bahamas on the same plane. If the flying the plane back also costs 5000 dollars, and does the company make an overall profit or loss? The company charges the same fee of 200 dollars per ticket for the return flight.

previous_profit = 800

cost_of_flying_plane = 5000
number_of_passengers = 12
price_of_ticket = 200
overall_profit = (price_of_ticket*number_of_passengers)-cost_of_flying_plane + previous_profit
print(overall_profit)
if overall_profit >0:
    print("The company makes an overall profit of {} dollars".format(abs(overall_profit)))
else:
    print("The company makes an overall loss of {} dollars".format(abs(overall_profit)))