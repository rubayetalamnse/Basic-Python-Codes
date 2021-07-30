fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) +fib.get(7, 5)) 
""" dictionary.get(key, optional_value)
So...
fib.get(4,0) = 3
din.get(7,5) = 5  # key value 7 not exists, so optional value 5 taken.
Adding both will give the answer. """