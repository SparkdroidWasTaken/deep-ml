import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	relu_d = 0 if x <= 0 else 1
	tanh_d = np.power(1 / np.cosh(x), 2)
	sig = 1 / (1 + np.exp(-x))
	sig_d = sig * (1 - sig)
	# Your code here
	return {'sigmoid': sig_d, 'tanh': tanh_d, 'relu': relu_d}
	pass