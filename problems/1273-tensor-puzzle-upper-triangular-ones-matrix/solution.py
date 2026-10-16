import numpy as np

def triu_ones(n: int) -> np.ndarray:
    """n x n upper-triangular matrix of ones (including diagonal)."""
    # Your code here
    mat = np.empty((n,n))
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i <= j:
                mat[i][j] = 1
    return np.round(mat)
    pass
