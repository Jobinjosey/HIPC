from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('seaborn-poster')
x = [1, 2, 3, 4]
y = [1, 5, 11, 8]


f = CubicSpline(x, y, bc_type='natural') # type natural for y"(0) = y"(3) = 0
x_new = np.linspace(0, 2, 100)
y_new = f(x_new)
plt.figure(figsize = (10,10))
plt.plot(x_new, y_new, 'b')
plt.plot(x, y, 'ro')
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
