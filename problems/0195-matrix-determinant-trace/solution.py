import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	A = np.array(matrix)
	tr = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if i==j:
				tr += matrix[i][j]
	return (np.linalg.det(A),tr)
	pass