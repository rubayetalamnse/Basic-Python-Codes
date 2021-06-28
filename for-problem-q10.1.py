#Calculate and display the sum of all the numbers divisible by 7 between 18 and 534 i.e. 21+28+35+...+525+532.
sum_of_numbers = 0
for i in range(18,535):
    if i%7 == 0:
        sum_of_numbers = sum_of_numbers + i

print('The sum of all the numbers divisible by 7 between 18 and 534 is', sum_of_numbers)
