#recursion means a function can call itself.
"""In the factorial program we saw:
5! = 5*4*3*2*1
4! = 4*3*2*1
3! = 3*2*1
2! = 2*1
1! = 1
n! = n*(n-1)!
 """

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))