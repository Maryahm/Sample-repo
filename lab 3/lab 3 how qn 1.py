# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:59:58 2024

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
def functn(xf):
    return np.sqrt(xf)*np.exp(-xf)
a=0.2
b=2
n= 5

xi = np.linspace(a,b,n)
h=(b-a)/n
fn = functn(xi)
x=[]
derv=[]
i=0
while i<n-2:
    f=(-fn[i+2]+4*fn[i+1]-3*fn[i])/(2*h)
    x.append(xi[i])
    derv.append(f)
    i+=1
    
print("value of y'(x) is", round(derv[i-1],4),"at x=",round(x[i-1],4))
plt.figure() 
plt.subplot(2,1,1)
plt.plot(xi,fn) 
plt.title('graph of $sqrt(x)*e^(-x)$ and dy/dx') 
plt.xlabel('x') 
plt.ylabel('y')
plt.subplot(2,1,2) 
plt.plot(x,derv) 
plt.xlabel('x') 
plt.ylabel("dy/dx")
plt.show()