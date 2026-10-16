import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Your code here
    #would b easy, but 0 vector sucks :/
    if len(vectors) == 0:
        return True
    elif len(vectors) == 1:
        return False if np.all(np.array(vectors[0])==0) else True
    else:
        return np.array_equal(np.array(vectors) @ np.transpose(np.array(vectors)), np.identity(len(vectors)))
    pass