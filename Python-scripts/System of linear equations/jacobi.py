
import numpy as np
import matplotlib.pyplot as plt


def jacobi(dim, A, B, X0, tol, n):
    """
    Arguments
    ---------
    dim: int
        Dimension of square matrix `A`
    A: 2D np.array
        Coefficient matrix
    B: np.array
        Constant matrix
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
        X1 = np.array(dim * [0.])
        for i in range(dim):
            for j in range(dim):
                X1[i] += (-A[i][j]*X0[j])
            X1[i] += A[i][i]*X0[i]
            X1[i] += B[i]
            X1[i] /= A[i][i]

        print('n:', iterations, 'X:', X1)

        epochs.append(iterations)
        x_one.append(X1[0])
        x_two.append(X1[1])
        x_three.append(X1[2])

        if np.max(abs(X0 - X1)) < tol:
            break
        iterations += 1
        X0 = X1
    return X1


A = np.array([
    [7, 1, 1],
    [-3, 7, -1],
    [-2, 5, 9]
], dtype=float)
B = np.array([6, -26, 1], dtype=float)

dim = A.shape[0]
tol = 1e-5
n = 10
# init_approx = np.array(dim * [0.])
init_approx = np.array([0, 0.5, 1])

# # check diagonal dominance
# for i in range(dim):
#     v1 = abs(A[i][i])
#     s = 0
#     for j in range(dim):
#         if i != j:
#             s += abs(A[i][j])
#     if s > v1:
#         print('A is not diagonally dominant. Change A and B accordingly')
#         exit()

epochs = []
x_one = []
x_two = []
x_three = []

jacobi(dim, A, B, init_approx, tol, n)

plt.plot(epochs, x_one, label='X1')
plt.plot(epochs, x_two, label='X2')
plt.plot(epochs, x_three, label='X3')

# naming the x axis
plt.xlabel('iterations')
# naming the y axis
plt.ylabel('X')
# giving a title to my graph
plt.title('Jacobi')
plt.legend(loc='upper left')
plt.show()
