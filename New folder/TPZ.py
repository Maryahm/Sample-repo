# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:38:55 2024

@author: User
"""
# trapezoidal rule
import numpy as np
import matplotlib.pyplot as plt
import math

def functn(x):
    y = x**2 + 1
    return y
a = -2
b = 4
n = 50
dx = (b - a) / n
sum = 0
i = 0

x1 = []
x2 = []
f1 = []
f2 = []
integer = []

while i < n:
    x11 = a + i * dx
    x1.append(x11)
    
    x22 = x11 + dx
    x2.append(x22)
    
    fn1 = functn(x11)
    fn2 = functn(x22)
    
    f1.append(fn1)
    f2.append(fn2)
    
    sum += dx * (fn1 + fn2) / 2
    integer.append(sum)
    
    i = i + 1

print("Integrated value =", round(sum, 3))

# Plotting the results
x_values = np.linspace(a, b, n)
f_values = [functn(x) for x in x_values]

plt.figure(figsize=(12, 6))

# Plot integer vs x
plt.subplot(1, 2, 1)
plt.plot(x1, integer, label='Integral of functn(x)')
plt.xlabel('x')
plt.ylabel('Integral')
plt.title('Integral vs x')
plt.legend()

# Plot functn(x) vs x
plt.subplot(1, 2, 2)
plt.plot(x_values, f_values, label='functn(x) = cos(x)^3')
plt.xlabel('x')
plt.ylabel('functn(x)')
plt.title('functn(x) vs x')
plt.legend()

plt.show()