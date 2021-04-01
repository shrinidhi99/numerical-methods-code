# Name: Shrinidhi Anil Varna
# Roll no: 171CO145
# Q no: 3

import numpy as np
import math
import matplotlib.pyplot as plt

# x
x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52, 2.77, 2.99])

# f(x)
y = np.array([0.23, -0.26, -1.1, -0.45, 0.27, 0.1, -0.29, 0.24, 0.56, 1])


x_l_l = 0 # log(x) * log(x)
x_l_c = 0 # log(x) * cos(x)
x_l_e = 0 # log(x) * exp(x)
x_c_c = 0 # cos(x) * cos(x)
x_c_e = 0 # cos(x) * exp(x)
x_e_e = 0 # exp(x) * exp(x)

y_l = 0 # y * log(x)
y_c = 0 # y * cos(x)
y_e = 0 # y * exp(x)


# finding the summation
for i in range(len(x)):
    x_l_l += math.log(x[i]) * math.log(x[i])
    x_l_c += math.log(x[i]) * math.cos(x[i])
    x_l_e += math.log(x[i]) * math.exp(x[i])
    x_c_c += math.cos(x[i]) * math.cos(x[i])
    x_c_e += math.cos(x[i]) * math.exp(x[i])
    x_e_e += math.exp(x[i]) * math.exp(x[i])

    y_l += y[i] * math.log(x[i])
    y_c += y[i] * math.cos(x[i])
    y_e += y[i] * math.exp(x[i])

# forming matrices with the above computed elements
A = np.array([[x_l_l, x_l_c, x_l_e],
              [x_l_c, x_c_c, x_c_e],
              [x_l_e, x_c_e, x_e_e]])

B = np.array([[y_l],
              [y_c],
              [y_e]])

X = np.dot(np.linalg.inv(A),  B)
# multiplying inverse of a matrix (A) to a matrix (B) to get the coefficients
print(X)

a = X[0]
b = X[1]
c = X[2]

# Error calculation

error = 0
# predicted value of y using the above coefficients

y_pred = []
for i in range(len(x)):
    error += (y[i] - ((a * math.log(x[i])) +
                      (b * math.cos(x[i])) + (c * math.exp(x[i])))) ** 2
    y_pred.append((a * math.log(x[i])) +
                  (b * math.cos(x[i])) + (c * math.exp(x[i])))

print(f'Error: {error}')
print(f'y_pred: {y_pred}')

plt.plot(x, y, label='Y_exact')
plt.plot(x, y_pred, label='Y predicted')

# naming the x axis
plt.xlabel('X')
# naming the y axis
plt.ylabel('Y')
# giving a title to my graph
plt.title('Least Square principle')
plt.legend(loc='upper left')
plt.show()
