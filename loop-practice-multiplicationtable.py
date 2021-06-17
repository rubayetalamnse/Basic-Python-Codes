num = int(input("enter the number of which multiplication table you want: "))
for i in range(1, 11):
    #print(str(num)+" x "+str(i) + " = " +str(i*num)) --->works
    #print(f"{num}*{i}={num*i}")---->works
    #print("{0} * {1} = {2}" .format(num,i,num*i))--->works
    print("{} * {} = {}" .format(num,i,num*i))
    i = i+1
