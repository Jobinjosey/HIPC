import numpy as np
def f(x, y):
    z = x+np.sin(y);
    return z;
  
def p(x, y, h):
      
    y1p = y + h * f(x, y);
    return y1p;

# using Modified Euler method
def correct(x, y, x1, y1, h):
      
    
    e = 0.05;
    y1c = y1;
  
    while (abs(y1c - y1) > e + 1):
        y1 = y1c;
        y1c = y + 0.5 * h * (f(x, y) + f(x1, y1));
  

    return y1c;
  
def printFinalValues(x, xn, y, h):
    while (x < xn):
        x1 = x + h;
        y1p = p(x, y, h);
        y1c = correct(x, y, x1, y1p, h);
        x = x1;
        y = y1c;
  
    
    print("The final value of y at x =",
                     int(x), "is :", y);
  
if __name__ == '__main__':
      
    
    x = 0; y = 1;
  
    # final value of x for which y is needed
    xn = 0.2;
  
    # step size
    h = 0.2;
  
    printFinalValues(x, xn, y, h);
  
