import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    X=np.array(X)
    mean=np.mean(X,axis=0)
    X_c=X-mean
    C=np.dot(X_c.T,X_c)/(len(X)-1)
    eigenvalues, eigenvectors = np.linalg.eig(C)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    W = eigenvectors[:, :k] 
    return np.dot(X_c,W)
    
    pass