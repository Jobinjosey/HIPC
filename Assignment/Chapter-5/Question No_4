###############################RK4 method########################################
import numpy as np
def dydx(x, y):
    return (x-y**2)
 
def rungeKutta(x0, y0, x, h):
    
    n = (int)((x - x0)/h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
 
        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 
        # Update next value of x
        x0 = x0 + h
    return y
 
# Driver method
x0 = 0
y = 1
x = 0.3
h = 0.1
print ('The value of y at x is:', rungeKutta(x0, y, x, h))
#####################################################################################################################################################
n = 24 
A = 0; B = 3.
t =[0]* 500; y =[0]* 500; yy =[0]*4
def f (t , y): 
    return( t-y**2)
def rk4 ( t , yy , h1 ) :
    for i in range (0 , 3) :
        t = h1 * i
        k0 = h1 * f (t , y[i ])
        k1 = h1 * f ( t + h1 / 2 , yy [ i ] + k0 / 2)
        k2 = h1 * f ( t + h1 / 2 , yy [ i ] + k1 / 2)
        k3 = h1 * f ( t + h1 , yy [ i ] + k2 )
        yy [ i + 1] = yy [ i ] + ( 1 / 6 ) * ( k0 + 2.* k1 + 2.* k2 + k3 )
        print ( i , yy [ i ] )
    return yy [3]
def ABM( a , b ,N) :
    h = (b−a) / N # step
    t [0 ] = a ; y [0 ] = 1.00; F0 = f ( t [0 ] , y [ 0 ] )
    for k in range (1 , 4) :
    t [k] = a + k * h
    y [1] = rk4 ( t [1] , y , h) # 1st step
    y [2] = rk4 ( t [2] , y , h) # 2nd s tep
    y [3] = rk4 ( t [3] , y , h) # 3rd step
    F1 = f ( t [1 ] , y [ 1 ] )
    F2 = f ( t [2 ] , y [ 2 ] )
    F3 = f ( t [3 ] , y [ 3 ] )
    h2 = h / 2 4.
    for k in range (3 , N) :
    p = y [ k ] + h2 *( −9 .* F0 + 37.* F1 − 59.* F2 + 55.* F3 )
    t [k + 1] = a + h *( k+1) # Next absc issa
    F4 = f ( t [ k+1] , p )
    y [ k+1] = y [ k ] + h2 *( F1−5.* F2 + 19.* F3 + 9.* F4 ) # Corrector
    F0 = F1 # Update va lues
    F1 = F2
    F2 = F3
    F3 = f ( t [ k + 1] , y [ k + 1 ] )
    return t,y
print ( " k t Y numerical Y exact" )
t , y = ABM(A, B , n )
for k in range (0 , n+1) :
print ( " %3d %5.3 f %12.11 f %12.11 f "
%(k , t [ k ] , y [ k ] , ( 3 . * exp(− t[k]/2.) −2.+ t [ k ] ) ) )


 

