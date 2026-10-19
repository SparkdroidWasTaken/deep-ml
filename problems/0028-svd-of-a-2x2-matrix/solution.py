import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    # Your code here
    y1 = A[1][0]+A[0][1]
    y2 = A[1][0]-A[0][1]
    x1 = A[0][0]-A[1][1]
    x2 = A[0][0]+A[1][1]

    h1 = np.sqrt(y1**2 + x1**2)
    h2 = np.sqrt(y2**2 + x2**2)

    s1 = (h1+h2)/2
    s2 = abs(h1-h2)/2
    sv = [s1,s2]
    #making U
    t1 = x1 / h1 if h1 > 0 else 1.0
    t2 = x2 / h2 if h2 > 0 else 1.0
    theta1 = np.copysign(0.5 * np.arccos(np.clip(t1, -1.0, 1.0)), y1)
    theta2 = np.copysign(0.5 * np.arccos(np.clip(t2, -1.0, 1.0)), y2)
    phi = (theta1 + theta2) / 2.0

    c, s = np.cos(phi), np.sin(phi)
    U = np.array([
        [c, -s],
        [s,  c]
    ])
    S = np.zeros((2,2))
    for i in range(2):
        for j in range(2):
            if i==j:
                S[i][j]= sv[i]
    
    V = np.linalg.inv(S) @ np.transpose(U) @ A 
    return U, sv, V
    

