# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:29:53 2024

@author: User
"""
#Plot a Graph of a Spiral motion with a radius of 2 units.

import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection = '3d')


theta = np.linspace(0,9*np.pi,100)
r = 2
a = r*theta

x = r*np.cos(theta)
y = r*np.sin(theta)
z = a*theta


ax.plot3D(x,y,z,"r")
ax.scatter(x,y,z,"g")