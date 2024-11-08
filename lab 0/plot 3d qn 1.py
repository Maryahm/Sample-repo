# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:50:06 2024

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
 
# creating an empty canvas
fig = plt.figure()
ax = plt.axes(projection="3d")

x=[0,1,2,3,4,5,6]
y=[0,1,4,9,16,25,36]
z=[0,1,4,9,16,25,36]
 
ax.plot3D(x, y, z, 'red')
ax.scatter(x, y, z, 'blue')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D plot for a curve passing through the given points')

