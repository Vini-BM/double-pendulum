import numpy as np


def fTheta1(theta1,theta2,dtheta1,dtheta2,g,l1,l2,m1,m2):
    beta = m2/(m1+m2*np.sin(theta1-theta2)**2)
    g_term = -g/l1 * (np.sin(theta1)*(1+beta*np.cos(theta1-theta2)**2) - beta*np.sin(theta2)*np.cos(theta1-theta2)) # term with gravity
    dtheta1_term = -beta*np.cos(theta1-theta2)*np.sin(theta1-theta2)*dtheta1**2 # term with angular velocity for theta1
    dtheta2_term = -m2/(m1+m2) * np.sin(theta1-theta2)*dtheta2**2 * (beta*np.cos(theta1-theta2)**2 + l2/l1) # same for theta2
    #simple = -g/l1 * np.sin(theta1) # term from simple pendulum
    #coupling = -(m2/(m1+m2)*l2/l1) * (np.cos(theta1-theta2)*dw2 + np.sin(theta1-theta2)*w2**2) # term from coupling
    return g_term + dtheta1_term + dtheta2_term

def fTheta2(theta1,theta2,dtheta1,dtheta2,g,l1,l2,m1,m2):
    alpha = (m1+m2)/(m1+m2*np.sin(theta1-theta2)**2)
    g_term = g/l2 * (np.sin(theta1)*np.cos(theta1-theta2)-np.sin(theta2)) # term with gravity
    dtheta1_term = l1/l2 * np.sin(theta1-theta2)*dtheta1**2 # term with angular velocity for theta1
    dtheta2_term = m2/(m1+m2) * np.sin(theta1-theta2)*np.cos(theta1-theta2)*dtheta2**2 # same for theta2
    #simple = -g/l2 * np.sin(theta2)
    #coupling = -l1/l2 * (np.cos(theta1-theta2)*dw1 - np.sin(theta1-theta2)*w1**2)
    return alpha * (g_term + dtheta1_term + dtheta2_term)

def integrate(theta1,theta2,dtheta1,dtheta2,tmax,dt,g,l1,l2,m1,m2):
    # Initialize time
    t = 0
    # Initialize lists
    theta1_list = [theta1]
    theta2_list = [theta2]
    dtheta1_list = [theta1]
    dtheta2_list = [theta2]
    t_list = [t]
    # Useful coefficient
    h = dt/2
    # Loop
    while t < tmax:

        # RK4 coefficients
        ## k: acceleration
        ## q: velocity

        # 1
        q1_t1 = dtheta1
        q1_t2 = dtheta2
        k1_t1 = fTheta1(theta1,theta2,dtheta1,dtheta2,g,l1,l2,m1,m2)
        k1_t2 = fTheta2(theta1,theta2,dtheta1,dtheta2,g,l1,l2,m1,m2)

        # 2
        q2_t1 = dtheta1 + k1_t1*h
        q2_t2 = dtheta2 + k1_t2*h
        k2_t1 = fTheta1(theta1+q1_t1*h, theta2+q1_t2*h, dtheta1+k1_t1*h, dtheta2+k1_t2*h, g,l1,l2,m1,m2)
        k2_t2 = fTheta2(theta1+q1_t1*h, theta2+q1_t2*h, dtheta1+k1_t1*h, dtheta2+k1_t2*h, g,l1,l2,m1,m2)

        # 3
        q3_t1 = dtheta1 + k2_t1*h
        q3_t2 = dtheta2 + q2_t2*h
        k3_t1 = fTheta1(theta1+q2_t1*h, theta2+q2_t2*h, dtheta1+k2_t1*h, dtheta2+k2_t2*h, g,l1,l2,m1,m2)
        k3_t2 = fTheta2(theta1+q2_t1*h, theta2+q2_t2*h, dtheta1+k2_t1*h, dtheta2+k2_t2*h, g,l1,l2,m1,m2)

        # 4
        q4_t1 = dtheta1 + q3_t1*dt
        q4_t2 = dtheta2 + q3_t2*dt
        k4_t1 = fTheta1(theta1+q3_t1*dt, theta2+q3_t2*dt, dtheta1+k3_t1*dt, dtheta2+k3_t2*dt, g,l1,l2,m1,m2)
        k4_t2 = fTheta2(theta1+q3_t1*dt, theta2+q3_t2*dt, dtheta1+k3_t1*dt, dtheta2+k3_t2*dt, g,l1,l2,m1,m2)

        # Update variables
        ## First mass
        dtheta1 += dt*(k1_t1 + 2*k2_t1 + 2*k3_t1 + k4_t1)/6 # angular velocity
        theta1 += dt*(q1_t1 + 2*q2_t1 + 2*q3_t1 + q4_t1)/6 # angle
        ## Second mass
        dtheta2 += dt*(k1_t2 + 2*k2_t2 + 2*k3_t2 + k4_t2)/6 # angular velocity
        theta2 += dt*(q1_t2 + 2*q2_t2 + 2*q3_t2 + q4_t2)/6 # angle
        ## Time
        t += dt

        # Save values
        theta1_list.append(theta1)
        theta2_list.append(theta2)
        dtheta1_list.append(dtheta1)
        dtheta2_list.append(dtheta2)
        t_list.append(t)

    return theta1_list, theta2_list, dtheta1_list, dtheta2_list, t_list
