# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 02:58:39 2024

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
def fxn(xy):
    return  xy**2
    
a = 1
b = 50
h= 100
n = b-a/h
xi = np.linspace(1,50,100)
fn = fxn(xi)

x = []
derv = []
i = 0

while i <n-2:
    f = (-fn[i+2] +4*fn[i+1]-3*fn[i])
    x.append(xi[i])
    derv.append(f)
    i = i +1
    
print(derv[i-1])

plt.plot(xi,fn) 
plt.plot(x,derv)