import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X=np.array(X, dtype=float)
    mean=np.mean(X,axis=0)
    X_c=X-mean
    cv=np.dot((X_c.T),X_c)/(X.shape[0]-1)
    return cv
    
    
    
    
    
    
    pass