# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:45:41 2024

@author: User
"""

#Plot a hyperbola : 8y^2 - 2x^2 = 16.
# we divide the equation by 16 and we get the formula here (to make the RHS = 1)

import numpy as np
import matplotlib.pyplot as plt

a = np.sqrt(2)
b = np.sqrt(8)

y = np.linspace(-4,4,40000)

xn = np.sqrt(((y**2/a**2)-1)*b**2)
xp = -np.sqrt(((y**2/a**2)-1)*b**2)

plt.plot(xn,y,'g',label = 'hyperbola')
plt.plot(xp,y,'g')

plt.plot((b/a)*y,y,'g--',label = 'Asymptotes',color = 'orange', )
plt.plot((-b/a)*y,y,'g--', color = 'orange')

plt.axvline(0, color = 'black')
plt.axhline(0,color = 'black')

plt.plot(0,0,'go')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Hyperbola")
plt.grid()
plt.legend(loc = 'best')
plt.show()