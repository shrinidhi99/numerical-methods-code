import numpy as np
from math import log


def curve_fit(x, y, deg=1):
    """
    Arguments
    ---------
    x: numpy.array
        x values
    y: numpy.array
        y value
    deg: int
        Degree of interpolated polynomial

    Returns
    -------
    np.array:
        Returns coefficients of polynomial
        [Starting from highest degree]
    """
    n = deg+1
    X = np.zeros((n, n))
    Y = np.zeros(n)

    # Initialize X
    for i in range(0, n):
        for j in range(0, n):
            X[i][j] = np.sum(x**(i+j))

    # Initialize Y
    for i in range(0, n):
        Y[i] = np.sum(y*x**(i))

    A = np.linalg.solve(X, Y)

    # compute error
    error = 0
    for i in range(len(x)):
        polyval = 0
        for j in range(0, len(A)):
            polyval += A[j]*(x[i])**j
        # print('polyval',polyval)
        error += (y[i] - polyval)**2
    print('Error:', error)

    A = np.flip(A)
    return A

x = np.array([1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83])
y = np.array([52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46])

deg = 1

A = curve_fit(x, y, deg)
print('Coefficients (highest power of x to lowest):', A)