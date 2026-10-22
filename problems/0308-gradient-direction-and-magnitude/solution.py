import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = np.sqrt(np.sum(np.array(gradient) **2))
	#0 check
	if magnitude == 0:
		return {'magnitude': magnitude, 'direction': np.zeros(len(gradient)), 'descent_direction': np.zeros(len(gradient))}
	else:
		return {'magnitude': magnitude, 'direction': gradient/magnitude, 'descent_direction': -(gradient/magnitude)}
	pass