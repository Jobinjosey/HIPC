import numpy as np
def func(x):
    return np.cos(x)-x**2-x
 
def derivFunc( x ):
    return -np.sin(x)-2*x-1
 
def newtonRaphson( x ):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
        x = x - h
    print("The value of the root is : ",
                             "%.4f"% x)
 
# Driver program to test above
x0 = -20 # Initial values assumed
newtonRaphson(x0)
