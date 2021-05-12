# Python program for implementation of Bisection Method

import numpy as np
import math

# The function is tanx + tanhx = 0
def func(x):
    return math.tan(x) + math.tanh(x)
  
# Prints root of func(x)
# with error of EPSILON
def bisection(a,b):
 
    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    while ((b-a) >= 0.01):
 
        # Find middle point
        c = (a+b)/2
  
        # Check if middle point is root
        if (func(c) == 0.0):
            break
  
        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c
             
    print("The value of root is : ","%.4f"%c)
     
# Driver code
# Initial values assumed
a = 2.3
b = 2.4
bisection(a, b)
