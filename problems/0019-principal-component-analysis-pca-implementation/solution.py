import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # Your code here
    #Find the means + stds of the columns
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0, ddof=0)
    
    # silly 0 error handling
    std[std == 0] = 1.0
    #standarise
    X_std = (data - mean) / std
    
    # Covar matrix
    n_samples = data.shape[0]
    cov_matrix = (X_std.T @ X_std) / n_samples
    
    #Find eigenvalues and eigenvectors
    evalues, evectors = np.linalg.eigh(cov_matrix)
    
    #Sort in descending order
    idx = np.argsort(evalues)[::-1]
    top_evectors = evectors[:, idx][:, :k]
    
    #Fix the sign so the first non-zero element of each eigenvector is positive
    for i in range(top_evectors.shape[1]):
        col = top_evectors[:, i]
        non_zero_idx = np.nonzero(col)[0]
        if len(non_zero_idx) > 0 and col[non_zero_idx[0]] < 0:
            top_evectors[:, i] = -col

    #Return rounded to 4 decimals
    return np.round(top_evectors, 4)