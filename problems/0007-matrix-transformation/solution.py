import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	#turn into numpy matrices so it easy
	a = np.array(A)
	t = np.array(T)
	s = np.array(S)
	if np.linalg.det(s) == 0 or np.linalg.det(t) == 0:
		return -1
	transformed_matrix1 = np.dot(np.linalg.inv(t),a)
	transformed_matrix = np.dot(transformed_matrix1,s)
	return transformed_matrix