import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    mean=np.mean(x)
    s=0
    for i in range(len(x)):
        s += (x[i]-mean)*(x[i]-mean)
    s=s/(len(x)-1)    
    s=np.sqrt(s)
    t=(mean-mu0)*(np.sqrt(len(x)))/s
    return float(t)
    pass