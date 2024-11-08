# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:20:10 2024

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6*np.pi, 100)
y = np.linspace(0,2*np.pi,100)
x,y = np.meshgrid(x,y)

z = np.cos(x) + np.sin(y)

ax = plt.axes(projection='3d')

ax.plot_surface(x,y,z)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_title("the 3d plot")
plt.show()

