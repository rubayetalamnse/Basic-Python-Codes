n =  int(input())

for i in range(0,n+1):
    if not i%2==0:
        if i%3==0:
            print("Solo",i)
        elif i%5 ==0:
            print("Learn",i)
        elif i%3 ==0 and i%5==0:
            print("SoloLearn",i)