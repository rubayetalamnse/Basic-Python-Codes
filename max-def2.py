def maximum_num(a, b):
    if a > b:
        return a
    else:
        return b

# function is defined, take value now


a = int(input("enter a number: "))
b = int(input("enter another number: "))
print("Larger of these two number is :", maximum_num(a, b))

#there is a built in function available in the python library called "max()", it's like print()
x = 56
y = 87
print(max(x, y))
