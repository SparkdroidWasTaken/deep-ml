import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    if vectors == [[0,0]] or len(vectors) <=1:
        return []
    vecs = []
    # Your code here
    #normalise the first vector
    norm_0 = np.linalg.norm(vectors[0])
    if norm_0 > tol:
        vecs.append(vectors[0] / norm_0)
    else:
        vecs.append(vectors[0])
    #now the others
    for i in range(1, len(vectors)):
        w = vectors[i].copy()
        
        # Summation step: subtract projections onto ALL previously stored basis vectors
        for e in vecs:
            w = w - np.dot(vectors[i], e) * e
            
        # Check tolerance and normalise the vector

        if np.linalg.norm(w) > tol:
            vecs.append(w / np.linalg.norm(w))
        elif np.all(w == 0):
            #we ignore w here
            pass
        else:
            vecs.append(w)
    
    return vecs