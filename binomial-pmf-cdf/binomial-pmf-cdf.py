import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf= math.comb(n,k)*math.pow(p,k)*math.pow(1-p,n-k)
    cdf=0
    for i in range(k+1):
        cdf += math.comb(n,i)*math.pow(p,i)*math.pow(1-p,n-i)
    return {"pmf":float(pmf), "cdf":float(cdf)}    
        
    pass