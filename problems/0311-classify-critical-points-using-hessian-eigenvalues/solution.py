import numpy as np

def classify_critical_point(hessian: np.ndarray, tol: float = 1e-10):
    eigen = np.linalg.eigvals(hessian)
    count = 0
    n = len(eigen)
    for e in eigen:
        if e > 0:
            count += 1
        elif e < 0:
            count -=1
        elif e == 0:
            return None
    if count == n:
        return -1
    elif count == -n:
        return 1
    else:
        return 0