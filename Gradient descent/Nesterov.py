import numpy as np 
import scipy.optimize as opt

def NAG(func, x0, alpha=0.01, beta=0.9, tol=1e-6, max_iter=1000):
    """
    Nesterov Accelerated Gradient (NAG) optimization algorithm.
    
    Parameters:
    - func: The objective function to minimize.
    - x0: Initial guess for the variables.
    - alpha: Learning rate.
    - beta: Momentum factor.
    - tol: Tolerance for convergence.
    - max_iter: Maximum number of iterations.
    
    Returns:
    - x: The optimized variables.
    """
    x=x0.copy()
    phi_prev = 0
    for i in range(max_iter):
        grad=opt.approx_fprime(x, func, epsilon=1e-8)
        phi= x - beta * grad
        x_prev = x.copy()
        x= phi + alpha * (phi - phi_prev)
        phi_prev = phi
        if np.linalg.norm(x - x_prev) < tol:
            return x
        x_prev = x.copy()
        phi_prev = phi.copy()
    return x
def NAG_scipy(func, x0, alpha=0.01, beta=0.9, tol=1e-6, max_iter=1000):
    """
    Nesterov Accelerated Gradient (NAG) optimization using scipy's minimize function.
    
    Parameters:
    - func: The objective function to minimize.
    - x0: Initial guess for the variables.
    - alpha: Learning rate.
    - beta: Momentum factor.
    - tol: Tolerance for convergence.
    - max_iter: Maximum number of iterations.
    
    Returns:
    - res: The result of the optimization.
    """
    res = opt.minimize(func, x0, method='Nelder-Mead', options={'maxiter': max_iter, 'disp': True})
    return res.x