import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

p=(1.09/2.09)
f=(1/2.09)

val = 20*(p**3)*(f**3)+15*(p**4)*(f**2)+6*(p**5)*f+(p**6)
print(round(val,3))

