def filter_even_numbers(number_list):
    result_list=[]
    for number in number_list:
        if number%2 == 0:
            result_list.append(number)
    print(result_list)
filter_even_numbers([1,2,3,4,5,6,7,8,9])
