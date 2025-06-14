def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)         # Number of vectors (features)
    n_samples = len(vectors[0])       # Number of samples in each vector

    means = []
    for feature in vectors:
        mean = sum(feature) / n_samples
        means.append(mean)

    covar = [[0.0 for _ in range(n_features)] for _ in range(n_features)]

    for i in range(n_features):
        for j in range(n_features):
            cov_ij = 0.0
            for k in range(n_samples):
                cov_ij += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
            cov_ij /= (n_samples - 1) 
            covar[i][j] = cov_ij

    return covar