import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X=np.array(X)
    X_c=X-np.mean(X,axis=0)
    cv=(np.dot((X_c.T),(X_c)))/(X.shape[0]-1)
    std=np.sqrt(np.diag(cv))
    denominator = np.outer(std, std)
    R = cv / np.where(denominator == 0, np.nan, denominator)
    return R              

    
    
    
    
    pass