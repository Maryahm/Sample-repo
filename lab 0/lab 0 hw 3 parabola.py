# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:13:07 2024

@author: User
"""

#Plot a parabola with focus at (0, 2) and directrix y = -2
#(equation for parabola is x^2=4ay, with focus (0, a) and directrix y = -a)
import numpy as np
import matplotlib.pyplot as plt


a = 2 # focus is (0,a)
y = np.linspace(-2,2,40000)
xp = np.sqrt(4*a*y)
xn = -np.sqrt(4*a*y)

plt.plot(xp,y,'r', label = 'parabola')
plt.plot(xn,y,'r')

plt.axhline(y = -2,linestyle = '-',color = 'b', label = 'directrix')

plt.plot(0,a,'go', label = 'focus')

plt.grid()
plt.legend()
plt.show()
