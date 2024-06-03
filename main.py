import numpy as np
import matplotlib.pyplot as plt
from integration import integrate
from equations import getCoordinates

m1, m2 = 1, 1
l1, l2 = 1, 1
lmax = l1+l2
g = 9.8

theta1, theta2 = 3, 1.2
dtheta1, dtheta2 = 0, 0

tmax = 10
dt = 0.01

t1_list, t2_list, d1_list, d2_list, time = integrate(theta1,theta2,dtheta1,dtheta2,tmax,dt,g,l1,l2,m1,m2)

"""
# Time plot
plt.plot(time,t1_list,label=r'$\theta_1(t)$')
plt.plot(time,t2_list,label=r'$\theta_2(t)$')
plt.xlabel(r'$t$')
plt.ylabel(r'$\theta_1$, $\theta_2$')
plt.title('Double pendulum')
plt.legend()
plt.show()
"""

# Trajectory plot
x1, y1, x2, y2 = getCoordinates(t1_list, t2_list, l1, l2)
plt.plot(x1,y1,label='First pendulum')
plt.plot(x2,y2,label='Second pendulum')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.xlim(-lmax,lmax)
plt.ylim(-lmax,lmax)
plt.title('Trajectory of the double pendulum')
plt.show()