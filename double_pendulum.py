import numpy as np
from matplotlib.animation import PillowWriter
from integration import integrate
from plots import trajectory
from sys import argv


def main(theta1,theta2,dtheta1,dtheta2,m1=1.,m2=1.,l1=1.,l2=1.,g=9.8,tmax=10):
    lmax = l1+l2
    t1_list, t2_list, d1_list, d2_list, time = integrate(theta1,theta2,dtheta1,dtheta2,tmax,g,l1,l2,m1,m2)
    pendulum = trajectory(t1_list,t2_list,m1,m2,l1,l2,g,time)
    #pendulum.save('doublePendulum.gif',writer=PillowWriter(fps=30)) # uncomment if you want to save animation

if __name__ == '__main__':
    if len(argv) == 1:
        theta1, theta2, dtheta1, dtheta2 = np.pi*np.random.rand(4)
        main(theta1, theta2, dtheta1, dtheta2) # random initial condition and default parameters
    else:
        theta1 = float(argv[1])
        theta2 = float(argv[2])
        dtheta1 = float(argv[3])
        dtheta2 = float(argv[4])
        m1 = float(argv[5])
        m2 = float(argv[6])
        l1 = float(argv[7])
        l2 = float(argv[8])
        g = float(argv[9])
        tmax = int(argv[10])
        main(theta1,theta2,dtheta1,dtheta2,m1,m2,l1,l2,g,tmax)