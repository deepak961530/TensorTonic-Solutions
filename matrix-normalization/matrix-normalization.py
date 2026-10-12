import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    X=np.array(matrix)
    if norm_type == "l1":
        norm = np.sum(np.abs(X), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norm = np.sqrt(np.sum(X**2, axis=axis, keepdims=True))
    elif norm_type == "max":
        norm =np.max(np.abs(X), axis=axis ,keepdims=True)

    norm= np.where(norm==0,1,norm)
    return X/norm
    pass