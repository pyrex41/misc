import numpy as np

def raw_moment(vec, r):
    return 1 / len(vec) * sum(list(map(lambda i: i**r, vec)))
    
def kelly(retvec, int=6):
    moms = []
    for i in range(int):
        moms.append(raw_moment(retvec, i+1))
    p = []
    for i in range(len(moms)):
        p.append((-1)**i * moms[i])
    r = np.polynomial.polynomial.polyroots(p)
    rr = r.real[abs(r.imag)<1e-5]
    return min(rr)
