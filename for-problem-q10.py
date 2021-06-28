#Calculate and display the sum of all the numbers divisible by 7 between 18 and 534 i.e. 21+28+35+...+525+532.
number_list =[]
for i in range(18,535):
    if i%7 == 0:
        number_list.append(i)

print("sum_of_numbers",sum(number_list))