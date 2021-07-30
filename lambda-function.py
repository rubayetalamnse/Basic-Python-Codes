#LAMBDA/ANONYMUS FUNCTION

def add(a,b):
    print(a+b)
add(5,5)

#doing it via lambda function:

adder = lambda x,y: x+y

print(adder(4,5)) 


#using function to sort a list.
def a_first(a):
    return a[0] #a[0]= first item (10,3,15,70,9)

a = [[10,2],[3,4],[15,6],[70,8],[9,10]]
a.sort(key=a_first)
print(a)
#output-------[[3, 4], [9, 10], [10, 2], [15, 6], [70, 8]]

#what if we do it by lambda function:
a = [[10,2],[3,4],[15,6],[70,8],[9,10]]
a.sort(key=lambda x: x[0])
print(a)
#output-------[[3, 4], [9, 10], [10, 2], [15, 6], [70, 8]]

#lambda function is like not making a function but working like a function...