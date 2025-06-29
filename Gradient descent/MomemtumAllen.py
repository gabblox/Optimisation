import numpy as np
import scipy.optimize as opt

def func_grad(func,x):
    """
    Compute the gradient of a function at a given point.
    """
    epsilon = 1e-8
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = np.copy(x)
        x_plus[i] += epsilon
        f_plus = func(x_plus)
        
        x_minus = np.copy(x)
        x_minus[i] -= epsilon
        f_minus = func(x_minus)
        
        grad[i] = (f_plus - f_minus) / (2 * epsilon)
    return grad

def Allen_Orrechia(func, x0, alpha,tau, max_iter=1000, tol=1e-6):
    x=x0
    y=x0
    z=x0
    L=(1-tau)/(alpha*tau)
    for i in range(max_iter):
        x_new=(1-tau)*y+tau*z
        grad = func_grad(func, x_new)
        z_new = z - alpha * grad
        y_new = x_new - (1/L) * grad
        if np.linalg.norm(x_new - x) < tol:
            print(f"Converged after {i+1} iterations.")
            return x_new
        x = x_new
        y = y_new
        z = z_new
    return x
