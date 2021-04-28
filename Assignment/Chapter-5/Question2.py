def func( x, y ):
    return (x*(y+x)-2)
     
# Function for euler formula
def euler( x0, y, h, x ):
    temp = -0
 
    # Iterating till the point at which we
    # need approximation
    while x0 < x:
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h
 
    # Printing approximation
    print("Approximate solution at x = ", x, " is ", "%.6f"% y)
     

x0 = 0
y0 = 2
h = 0.015
 
# Value of x at which we need approximation
x = 0.6
 
euler(x0, y0, h, x)
