import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

plt.rcParams.update({
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

dt = 0.01 # fixed on integration

def getCoordinates(theta1,theta2,l1,l2):
    """
    Returns the cartesian coordinates (x1,y1) and (x2,y2) for both masses on the double pendulum.
    """

    # First mass
    x1 = l1*np.sin(theta1)
    y1 = -l1*np.cos(theta1)
    # Second mass
    x2 = x1 + l2*np.sin(theta2)
    y2 = y1 - l2*np.cos(theta2)

    return x1, y1, x2, y2

def angleTime(time,dt,theta1,theta2,lmax):
    """
    Animates the angles theta1 and theta2 as a function of time.
    """

    # Initialize plot
    fig, ax = plt.subplots()
    p1 = ax.plot(time[0],theta1[0],label=r'$\theta_1(t)$')[0]
    p2 = ax.plot(time[0],theta2[0],label=r'$\theta_2(t)$')[0]
    ax.set(xlabel=r'$t$', ylabel=r'$\theta_1$, $\theta_2$', title='Double pendulum')
    ax.legend()

    # Animation function
    def animate(i):
        p1.set_data(time[:i],theta1[:i])
        p2.set_data(time[:i],theta2[:i])
        ax.set_xlim([0,time[:i]])
        return p1, p2

    # Create animation
    ani = FuncAnimation(fig=fig, func=animate, frames=len(time), interval=dt)
    plt.show()
    return ani

def trajectory(theta1,theta2,m1,m2,l1,l2,g,time):
    """
    Animates the trajectory for the double pendulum given the time evolution of theta1 and theta2
    as well as the system's parameters.
    """

    # Coordinates
    lmax = l1+l2 # maximum radius for pendulum
    x1, y1, x2, y2 = getCoordinates(theta1,theta2,l1,l2) # cartesian coordinates

    # Initialize plot
    fig, ax = plt.subplots()
    structure, = ax.plot([], [], 'o-', color='blue') # plots the pendulum itself
    trace, = ax.plot([], [], color='red') # plots the trace of the second mass
    p1 = ax.plot(x1[0],y1[0],color='blue')[0] # plots initial position of first pass
    p2 = ax.plot(x2[0],y2[0],color='red')[0] # plots initial position of second mass
    ax.set(xlim=[-lmax, lmax], ylim=[-lmax, lmax], xlabel=r'$x$', ylabel=r'$y$') # sets limits
    ax.set_title(rf'$m_1 = {m1:.1f}$ | $m_2 = {m2:.1f}$ | $l_1 = {l1:.1f}$ | $l_2 = {l2:.1f}$ | $g = {g:.1f}$') # sets title with paramters
    counter = ax.text(-lmax*.95,lmax*.9, '') # sets text location for displaying time

    # Animation function
    def animate(i):

        frame = 3*i # 3 frames per iteration for efficiency

        # Plots current pendulum position
        current_x = [0, x1[frame], x2[frame]] # x coordinate of center and both masses
        current_y = [0, y1[frame], y2[frame]] # y coordinate of center and both masses
        structure.set_data(current_x, current_y) # updates data

        # Plots trajectory of second mass
        past_x2 = x2[:frame] # x coordinate until current time
        past_y2 = y2[:frame] # y coordinate until current time
        trace.set_data(past_x2, past_y2) # updates trace

        # Sets time counter
        counter.set_text(f'Time = {frame*dt:.2f}')

        return structure, trace

    # Create animation
    ani = FuncAnimation(fig=fig, func=animate, frames=int(len(time)/3), interval=dt/3*1000)
    plt.show()
    return ani

