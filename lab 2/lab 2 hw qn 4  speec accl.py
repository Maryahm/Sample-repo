# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:41:24 2024

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise acceleration function
def acceleration(t):
    if 0 <= t < 5:
        return 0
    elif 5 <= t < 10:
        return 5
    elif 10 <= t < 15:
        return 0
    elif 15 <= t < 20:
        return -5
    elif 20 <= t <= 25:
        return 0

# Initialize variables
a = 0
b = 25
n = 500
dt = (b - a) / n

time = np.linspace(a, b, n)
acc = [acceleration(t) for t in time]

speed = []
displacement = []
v = 0
x = 0

# Numerical integration to calculate speed and displacement
for i in range(n):
    v += acc[i] * dt
    x += v * dt
    speed.append(v)
    displacement.append(x)

# Plotting the results
plt.figure(figsize=(12, 6))

# Plot speed vs time
plt.subplot(2, 1, 1)
plt.plot(time, speed, label='Speed')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.title('Speed vs Time')
plt.legend()
plt.grid(True)

# Plot displacement vs time
plt.subplot(2, 1, 2)
plt.plot(time, displacement, label='Displacement', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Displacement vs Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
