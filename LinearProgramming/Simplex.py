import numpy as np

class Simplex:
    def __init__(self, c, A, b):
        """
        Initialize the Simplex solver with the objective function coefficients,
        constraint coefficients, and right-hand side values.

        Parameters:
        c : array_like
            Coefficients of the objective function.
        A : array_like
            Coefficients of the inequality constraints.
        b : array_like
            Right-hand side of the inequality constraints.
        """
        self.c = np.array(c)
        self.A = np.array(A)
        self.b = np.array(b)
    def simplex(self,c, A, b):
        """
        Solve the linear programming problem:
            maximize c^T * x
            subject to A * x <= b
            x >= 0

        Parameters:
        c : array_like
            Coefficients of the objective function.
        A : array_like
            Coefficients of the inequality constraints.
        b : array_like
            Right-hand side of the inequality constraints.

        Returns:
        x : ndarray
            Solution vector that maximizes the objective function.
        """
        m, n = A.shape
        base=self.real_base(A,b)
        c_b=c[:m]
        c_n=c[m:]
        pi=np.dot(c_b, np.linalg.inv(base))
        
        
    def real_base(self, A, b):
        return