import numpy as np
from math import inf


def newton_raphson(F, J, X, tol, n):
    """
    Arguments
    ---------
    F: function
        Function returning vector of functions
    J: function returning a matrix
        Function returning Jacobian matrix
    X: np.array
        Initial approximation vector
    tol: float
        tolerance
    n: int
        maximum number of iterations
    """

    print('n:', 0, 'X:', X)
    iterations = 1
    while iterations <= n:
        # Calculate error vector
        E = -np.dot(np.linalg.inv(J(X)), F(X))
        X = X + E
        print('n:', iterations, 'X:', X)
        if np.max(abs(E)) < tol:
            break
        iterations += 1
    return X


def f(X): return X[0]**2 - X[1]**2 - 3


def g(X): return X[0]**2 + X[1]**2 - 13


def F(X): return np.array([f(X), g(X)])

# partial derivatives w.r.t each xi


def fx0(X): return 2*X[0]


def fx1(X): return -2*X[1]


def gx0(X): return 2*X[0]


def gx1(X): return 2*X[1]


def J(X): return np.array([
    [fx0(X), fx1(X)],
    [gx0(X), gx1(X)]
])


initial_approx = np.array([1.5, 0.5])
tol = 1e-6
n = 10

newton_raphson(F, J, initial_approx, tol, n)

# Use this for <= 3 variables
# f = lambda x, y: x**2 + x*y + y**2 - 7
# g = lambda x, y: x**3 + y**3 - 9

# F = lambda X: np.array([f(*X), g(*X)])

# fx = lambda x, y: 2*x + y
# fy = lambda x, y: x + 2*y
# gx = lambda x, y: 3*x**2
# gy = lambda x, y: 3*y**2

# J = lambda X: np.array([
#     [fx(*X), fy(*X)],
#     [gx(*X), gy(*X)]
# ])

# initial_approx = np.array([1.5, 0.5])
# tol = 1e-6
# n = inf

# newton_raphson(F, J, initial_approx, tol, n)
