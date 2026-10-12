from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean=0
    for i in range(len(x)):
        mean += x[i]
    mean=mean/len(x)
    x.sort()
    if(len(x)%2==0):
        median=float((x[len(x)//2-1]+x[len(x)//2])/2)
    else:
        median=float(x[len(x)//2])
    count=Counter(x)
    mode=count.most_common(1)[0][0]
    return {"mean": float(mean), "median":float(median), "mode":float(mode)}
    
    pass