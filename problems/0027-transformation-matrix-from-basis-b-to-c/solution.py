import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	b = np.array(B)
	c = np.array(C)
	c_i = np.linalg.inv(C)

	return c_i @ b