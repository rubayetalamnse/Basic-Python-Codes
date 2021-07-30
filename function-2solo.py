def mc():
    return 0
    print(4)

print(mc())

#functions can be used as objects in other functions:
def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

#how it works:
#see line 12
#add(add(x, y), add(x,y))
#add(add(5,10), add(5,10))
#add(15,15)
#30

#practice-soloLearn:

def square(x):
    return x*x

def test(func,x):
    print(func(x))

test(square,42)

'''This is a code for creation of a shape whitout using for loops, just with defining the functions, Void Functions'''

def two (f):
    f()
    f()
def four(n):
    two(n)
    two(n)
#First row definition
def p1 ():
    print('+ ----- ',end='')
#One column definition
def p2 ():
    print('|       ',end='')
#Repeating the row
def p3 ():
    two(p1)
    print('+')
#Repeating the column
def p4 ():
    two(p2)
    print('|')
def p5 ():
    four(p4)
def p6 ():
    p3()
    p5()
    p3()
    p5()
    p3()
p6()


#practice: 

def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)
#nothing is asked for returning. So the code will stop as sson as it reaches return. output---0


#practice: 
def munc(g):
    result = 0
    for i in range(g):
        result += i
        return result

print(munc(4))

""" first loop 
result = 0(the value of result) + 0 (value of i in first loop) = 0
second loop: 
result = 0(current value of result) + 1 (value of i in second loop) =1
third loop: 
result = 1(current value of result) + 2 (value of i in third loop) =3
fourth loop: 
result = 3(current value of result) + 3 (value of i in third loop) =6

#range = 4 so the value of i will be from 0 to 3.
"""