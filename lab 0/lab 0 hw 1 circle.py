# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 12:24:31 2024

@author: User
"""
#Plot a circle with a radius = 3 units.

import numpy as np
import matplotlib.pyplot as plt

r = 3
theta = np.linspace(0,2*np.pi,100)
x = r*np.cos(theta)
y = r*np.sin(theta)


plt.plot(x, y,'r')
plt.plot(0,0,'go')
plt.axis("equal")
plt.title("circle")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.show()