import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    mean=np.mean(x)
    sv=0
    for i in range(len(x)):
        sv+= (x[i]-mean)*(x[i]-mean)
    sv=sv/(len(x)-1)
    return {"variance":float(sv),"standard_deviation":float(np.sqrt(sv))}

    pass