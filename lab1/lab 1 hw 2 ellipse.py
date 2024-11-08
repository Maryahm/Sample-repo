# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:38:19 2024

@author: User
"""
#Plot a surface of an elliptical paraboloid x^2/64+y^2/9=z

import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection = '3d')

a = 8
b = 3
theta = np.linspace(0,2*np.pi, 100)


x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

x,y = np.meshgrid(x,y)
z = (x**2/a**2)+(y**2/b**2)

ax.plot_surface(x,y,z,cmap ='viridis')
plt.show()
