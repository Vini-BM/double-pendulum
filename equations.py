import numpy as np

def getCoordinates(theta1,theta2,l1,l2):
	# First
	x1 = l1*np.sin(theta1)
	y1 = -l1*np.cos(theta1)
	# Second
	x2 = x1 + l2*np.sin(theta2)
	y2 = y1 - l2*np.cos(theta2)

	return x1, y1, x2, y2
