# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 02:18:17 2024

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

def func(xn,yn):
    return xn * 6*yn**2

a = 1
b = 3
h = 0.05
n = (b-a)/h
x = []
y = []
i = 0

x.append(0)
y.append(1/25)

while i<n:
    x.append(a + h*(i+1))
    y.append(y[i] + h* func(x[i],y[i]))
    i = i+1
     
print (x[i],y[i])
plt.plot(x,y)
plt.show()