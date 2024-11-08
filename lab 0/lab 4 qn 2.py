# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:39:42 2024

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x, y) for the differential equation dy/dx = y + x
def fxy(xf, yf):
    return 6*(yf**2)*xf

# Parameters
a = 1       # Initial x value
b = 3       # Final x value
h=0.0001                                                                                                                                                          # Number of steps
n= int((b - a) /h)# Step size

# Initialize arrays to store x and y values
x = []
y = []

# Initial values
x.append(1)
y.append(0.04)   # y(0) = 1

# Euler's Method
for i in range(n):
    x_next = a + h * (i + 1)
    y_next = y[i] + h * fxy(x[i], y[i])
    x.append(x_next)
    y.append(y_next)

# Print the final result
print('Value of y(x)', round(y[-1], 6), "at x =", x[-1])

# Plotting the results
plt.plot(x, y)
plt.title('Solution of DE $dy/dx = y + x$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()