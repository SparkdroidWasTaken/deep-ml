import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    x = np.array(X)
    target = np.array(y)
    theta = np.dot((np.dot(np.linalg.inv(np.dot(x.T,x)),x.T)),target)
	return theta