import numpy as np
def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    # Predictions
    y_pred = X @ w
    
    # Mean Squared Error (MSE)
    mse = np.mean((y_true - y_pred) ** 2)
    
    # Ridge regularization term (L2 norm squared of coefficients)
    regularization = alpha * np.sum(w ** 2)
    
    # Total Ridge loss
    return mse + regularization

