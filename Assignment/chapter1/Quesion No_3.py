#####################################################################################################################################################################3
#####################Newton Raphson Method########################################

def func( x ):
    return x * x * x - x * x + 2
 
def derivFunc( x ):
    return 3 * x * x - 2 * x
 

def newtonRaphson( x ):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
         
    
        x = x - h
     
    print("The value of the root is : ",
                             "%.4f"% x)
 

x0 = 0.8 # Initial values assumed
newtonRaphson(x0)
 
###################################################################################################################################################################3
##################################Secant Method###########################################################################################################33

def f(x):
    f = x**3-x**2-x+1;
    return f;
 
def secant(x1, x2, E):
    n = 0; xm = -1; x0 = 0; c = 0;
    if (f(x1) * f(x2) < 0):
        while True:
             
            # calculate the intermediate value
            x0 = ((x1 * f(x2) - x2 * f(x1)) /
                            (f(x2) - f(x1)));
 
            # check if x0 is root of
            # equation or not
            c = f(x1) * f(x0);
 
            # update the value of interval
            x1 = x2;
            x2 = x0;
 
            # update number of iteration
            n += 1;
 
            # if x0 is the root of equation
            # then break the loop
            if (c == 0):
                break;
            xm = ((x1 * f(x2) - x2 * f(x1)) /
                            (f(x2) - f(x1)));
             
            if(abs(xm - x0) < E):
                break;
         
        print("Root of the given equation =",
                               round(x0, 6));
        print("No. of iterations = ", n);
         
    else:
        print("Can not find a root in ",
                   "the given inteval");
 
# Driver code
 
# initializing the values
x1 = 0;
x2 = 2;
E = 0.001;
secant(x1, x2, E);
########################################################################################################################################################
############################Muller Method###########################################################################################################3

import math;
import numpy as np
 
MAX_ITERATIONS = 10000;
 

def f(x):
    return (1 * pow(x, 3) +  x * x 
                        - x +1);
 
def Muller(a, b, c):
 
    res = 0;
    i = 0;
 
    while (True):
     
        
        f1 = f(a); f2 = f(b); f3 = f(c);
        d1 = f1 - f3;
        d2 = f2 - f3;
        h1 = a - c;
        h2 = b - c;
        a0 = f3;
        a1 = (((d2 * pow(h1, 2)) -
               (d1 * pow(h2, 2))) /
              ((h1 * h2) * (h1 - h2)));
        a2 = (((d1 * h2) - (d2 * h1)) /
              ((h1 * h2) * (h1 - h2)));
        x = ((-2 * a0) / (a1 +
             abs(np.sqrt(a1 * a1 - 4 * a0 * a2))));
        y = ((-2 * a0) / (a1 -
            abs(np.sqrt(a1 * a1 - 4 * a0 * a2))));
 
        # Taking the root which is
        # closer to x2
        if (x >= y):
            res = x + c;
        else:
            res = y + c;
 
        # checking for resemblance of x3
        # with x2 till two decimal places
        m = res * 100;
        n = c * 100;
        m = np.floor(m);
        n = np.floor(n);
        if (m == n):
            break;
        a = b;
        b = c;
        c = res;
        if (i > MAX_ITERATIONS):
            print("Root cannot be found using",
                            "Muller's method");
            break;
        i += 1;
    if (i <= MAX_ITERATIONS):
        print("The value of the root is",
                          round(res, 4));
 

a = 0;
b = 1;
c = 2;
Muller(a, b, c);
     
