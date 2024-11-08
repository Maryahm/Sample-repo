# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:34:16 2024

@author: User
"""

# midpoint method

import math
import matplotlib.pyplot as plt

def functn(x):
    y = x**2 + 1
    return y

a = -2 #lower limit
b = 4 #upper limit
n = 50
dx = (b-a)/n # width of each interval
sum = 0
i = 0

x = []
f = []
integ = []

while i <n:
    #getting mid point
    midpt = a + i*dx + 1/2 *dx
    
    
    x.append(midpt)
    fn = functn(midpt)
    f.append(fn)
    sum = sum + f[i]*dx
    integ.append(sum)
    i = i +1
    
print("integrated value = ", round(sum,3))

#plotting f-x

plt.figure()
plt.subplot (2,1,1)
plt.plot(x,f)
plt.title("graph of f(x) = x and $\int f(x) dx$")
plt.xlabel('x')
plt.ylabel ('f(x)')

plt.subplot(2,1,2)
plt.plot(x,integ)
plt.xlabel ('x')
plt.ylabel('$\int_{a}^{b} f(x) dx$')

plt.show()