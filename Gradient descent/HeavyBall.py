import numpy as np 
import scipy.optimize as opt

def Heavy_ball(f, x0, alpha=0.1, beta=0.9, tol=1e-6, max_iter=1000):
    m=opt.approx_fprime(x0, f, epsilon=1e-8)
    x = x0.copy()
    for i in range(max_iter):
        m_new= beta*m - (1-beta)*opt.approx_fprime(x, f, epsilon=1e-8)
        x_new = x - alpha * m_new
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
        m = m_new
    return x
