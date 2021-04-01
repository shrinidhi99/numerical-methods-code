import numpy as np
import math

# x
x = [-1, 0, 1, 1.5]
# f(x)
y = [3.1, 0.9, 2.9, 2]

# contents of the two matrices A and B
x_2 = 0
x_3 = 0
x_4 = 0
x_y = 0
x_2_y = 0

# finding the summation
for i in range(len(x)):
    x_2 += x[i] ** 2
    x_3 += x[i] ** 3
    x_4 += x[i] ** 4
    x_y += x[i] * y[i]
    x_2_y += (x[i] ** 2) * y[i]

# forming matrices with the above computed elements
A = np.array([[x_2, x_3],
              [x_3, x_4]])

B = np.array([[x_y],
              [x_2_y]])

# multiplying inverse of a matrix (A) to a matrix (B) to get the coefficients 
print(np.dot(np.linalg.inv(A),  B))
