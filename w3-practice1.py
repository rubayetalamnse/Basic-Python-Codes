#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 

list = []
for num in range(1500,2701):
    if num%7==0 and num%5==0:
        list.append(str(num))
print (','.join(list))
