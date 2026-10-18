import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    MSE=0
    for i in range(len(y_pred)):
        MSE+= (y_pred[i]-y_true[i])*(y_pred[i]-y_true[i])
    return float(MSE/len(y_pred))    
    pass