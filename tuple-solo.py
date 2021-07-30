#nested tuple--- tuple inside a tuple:
tuple = (1, (1, 2, 3))
print(tuple[1])

#swapping values using tuple:----
a,b=(1,2)
print(a)
print(b)
a,b = b,a,
print("swapping values:")
print(a)
print(b)