import numpy as np 
import scipy.optimize as opt

def gradient_descent(func, x0, learning_rate=0.01, max_iter=1000, tol=1e-6):
    """
    Perform gradient descent to minimize a function.
    """
    x = np.copy(x0)
    for i in range(max_iter):
        grad = func_grad(func, x)
        x_new = x - learning_rate * grad
        
        if np.linalg.norm(x_new - x) < tol:
            print(f"Converged after {i+1} iterations.")
            return x_new
        
        x = x_new
    return x

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

def chain_grad(func1,func2,x0):
    grad2 = func_grad(func2, x0)
    grad1=func_grad(func1,func2(x0))
    return np.dot(grad1, grad2)

def optimize_with_scipy(func, x0):
    result = opt.minimize(func, x0)
    return result.x,result.func(result.x)

def scipy_grad(func, x0):
    """
    Compute the gradient of a function using scipy's numerical gradient.
    """
    return opt.approx_fprime(x0, func, epsilon=1e-8)