# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:00:46 2024

@author: User
"""
#Plot an ellipse 169/x^2 + 25/y^2 = 4225.

import numpy as np
import matplotlib.pyplot as plt

a = 5
b = 13
z = 1
theta = np.linspace(0,2*np.pi,100)

x = a*np.cos(theta)
y = b*np.sin(theta)

plt.plot(x,y,'g')
plt.axis("equal")
plt.xlabel("x-axis")
plt.ylabel("y=axis")
plt.title("Ellipse")
plt.grid()
plt.show()
