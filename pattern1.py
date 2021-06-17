no_rows = int(input("enter the number of rows "))

for row in range(1,no_rows+1):
    for column in range(1,row+1):
        print("*", end=" ") #this is for column
    print() #this is for row ----> this will print lines

