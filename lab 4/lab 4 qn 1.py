# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:39:25 2024

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
def fxy(xf,yf):
  y=yf+xf
  return y
a=0
b=1
n= 0.5
h=(b-a)/n
i=0
x=[]
y=[]
intg=[]

x.append(0)
y.append(1)
while i<n:
  x.append(a+h*(i+1))
  y.append(y[i]+h*fxy(x[i],y[i]))
  i+=1
print('Value of y(x)', round(y[i],6),"at x= ",x[i])
plt.plot(x,y)
plt.title('Solution of DE $dy/dx=y$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()