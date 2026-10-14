import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    X=np.array(X,dtype=float)
    mean=np.mean(X,axis=axis,keepdims=True)
    std=np.std(X,axis=axis,keepdims=True)
    std=np.where(std>eps,std,1.0)
    z=(X-mean)/std
    return z
    
    pass