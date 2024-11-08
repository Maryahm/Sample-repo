# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:32:22 2024

@author: User
"""

#Plot the planetary orbits of the solar system considering the fact that all planets revolve 
#around the sun in elliptical orbit with sun at one of the foci using following information 
#about the Solar system. [for ellipse focus (c, 0) and (-c, 0) where is c is given by c=a.e
# and b=sqrt(a^2-c^2 )
#1 A.U. = 149597870700 m,    Radius of Sun = 0.00464 AU


import numpy as np
import matplotlib.pyplot as plt

planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto","Halleys_comet"]
e = [0.2056,0.0068,0.0167,0.0934,0.0484,0.0542,0.0472,0.0086,0.2488,0.9671
]#eccentricity
a =[0.387,0.723,1.000,1.524,5.203,9.537,19.191,30.069,39.482,17.834
] #semi major axis


theta = np.linspace(0,2*np.pi,100)

r = 0.00464*149597870700


def c(a,e):
    return a*e

def b(a,c):
    return np.sqrt(a**2-c**2)

for i in range(len(planets)):
    ai = a[i]
    ei = e[i]
    ci = ai * ei
    bi = b(ai,ci)
    
    x = ai*np.cos(theta) - ci
    y = bi*np.sin(theta)
    
    plt.plot(x,y, label =f'{planets[i]}')
    


plt.plot(0,0,label ='focus (SUN')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend(loc = 'best')
plt.title("planetary orbits of solar system")
plt.grid()
plt.show()




