import numpy as np
from math import sqrt as s
def check_positive_definite(matrix: list) -> dict:
    """
    Check if a matrix is positive definite and compute its eigenvalues.
    
    Args:
        matrix: A 2D list representing a square matrix
        
    Returns:
        dict with 'is_positive_definite' (bool) and 'eigenvalues' (list of floats sorted ascending)
    """
    # Your code here
    #find the eigenvalues:
    eigenvalues = np.linalg.eigvals(matrix)
    Eigen = np.sort(eigenvalues)
    eig_list = [float(e) for e in Eigen]
    eig_r_list = [round(e,4) for e in eig_list]
    # Check if all eigenvalues are strictly positive
    is_pd = all(e > 0 for e in eig_r_list)
        
    return {
        'is_positive_definite': is_pd,
        'eigenvalues': eig_r_list
    }