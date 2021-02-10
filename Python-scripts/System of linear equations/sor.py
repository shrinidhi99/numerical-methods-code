import numpy as np
import matplotlib.pyplot as plt


def SOR(dim, A, B, ω, X0, tol, n):
    """
    Arguments
    ---------
    dim: int
        Dimension of square matrix `A`
    A: 2D np.array
        Coefficient matrix
    B: np.array
        Constant matrix
    ω: float
        Weigth to residual part of Gauss-Siedel method
    X0: np.array
        Initial approximation
    tol: float
        tolerance
    n: int
        maximum number of iterations
    """
    print('n:', 0, 'X:', X0)

    epochs.append(0)
    x_one.append(X0[0])
    x_two.append(X0[1])
    x_three.append(X0[2])

    iterations = 1
    while iterations <= n:
        X1 = np.array(dim*[0.])
        for i in range(dim):
            for j in range(i):
                X1[i] += (-A[i][j]*X1[j])
            for j in range(i+1, dim):
                X1[i] += (-A[i][j]*X0[j])
            X1[i] += B[i]
            X1[i] /= A[i][i]

            X1[i] *= ω
            X1[i] += (1-ω)*X0[i]

        print('n:', iterations, 'X:', X1)
        x_two.append(X1[1])
        x_three.append(X1[2])

        if np.max(abs(X0 - X1)) < tol:
            break
        iterations += 1
        X0 = X1
    return X1


A = np.array([
    [-10, -8, 0],
    [-8, 10, -1],
    [0, -1, 10]
], dtype=float)
B = np.array([-6, 9, 28], dtype=float)

dim = A.shape[0]
tol = 1e-5
n = 20
ω = 1.05
init_approx = np.array(dim * [0.])

# check diagonal dominance
for i in range(dim):
    v1 = abs(A[i][i])
    s = 0
    for j in range(dim):
        if i != j:
            s += abs(A[i][j])
    if s > v1:
        print('A is not diagonally dominant. Change A and B accordingly')
        exit()

epochs = []
x_one = []
x_two = []
x_three = []

SOR(dim, A, B, ω, init_approx, tol, n)

plt.plot(epochs, x_one, label='X1')
plt.plot(epochs, x_two, label='X2')
plt.plot(epochs, x_three, label='X3')

# naming the x axis
plt.xlabel('iterations')
# naming the y axis
plt.ylabel('X')
# giving a title to my graph
plt.title('SOR')
plt.legend(loc='upper left')
plt.show()
