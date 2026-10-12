import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    rows=[]
    for i in range(len(x)):
        if x[i]==0:
            rows.append(1-p)
        else :
            rows.append(p)
    mean=p
    variance=p*(1-p)
    rows=np.array(rows)
    return {"pmf": rows, "mean": float(mean), "variance": float(variance)}
    # Write code here
    pass