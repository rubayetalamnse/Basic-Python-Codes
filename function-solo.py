def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def pr(f1,f2,d):
    print(f1(f2(d+1,d),d))

pr(mult,sub,4)