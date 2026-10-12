import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    numerator=np.dot(a,b)
    denominator=np.linalg.norm(a)*np.linalg.norm(b)
    if denominator ==0:
        return 0.0
    return float(numerator/denominator)    
    
    
        
    pass