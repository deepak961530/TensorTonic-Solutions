import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    e=0
    for i in range(len(x)):
        e += float(x[i]*p[i])
    return e    
    pass