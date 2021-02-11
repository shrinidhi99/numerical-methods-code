# Name: Shrinidhi Anil Varna (171CO145)

import math
import matplotlib.pyplot as plt

# Defining Function


def f(x):
    return x**3 - 1.2*x**2 - 8.19*x + 13.23

# Defining derivative of function (f')


def g(x):
    return 3*x**2 - 2.4*x - 8.19

# Defining double derivative of function (f'')


def h(x):
    return 6*x - 2.4

# Implementing Newton Raphson Method


def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        prev_x0 = x0
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.7f and f(x1) = %0.7f' % (step, x1, f(x1)))
        nr_epochs.append(step)
        nr_x1_val.append(x1)
        nr_fx_val.append(f(x1))

        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        # uncomment this if you want function value to be within error
        # condition = abs(f(x1)) > e
        nr_error.append(x1 - prev_x0)
        # here, root value is considered for error
        condition = abs(x1 - prev_x0) > e and f(x1) != 0 and abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Implementing Modified Newton Method


def newtonRaphsonMultiRoot(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0)**2 - f(x0)*h(x0) == 0.0:
            print('Divide by zero error!')
            break

        prev_x0 = x0
        x1 = x0 - (f(x0) * g(x0))/(g(x0)**2 - f(x0)*h(x0))
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))

        nm_epochs.append(step)
        nm_x1_val.append(x1)
        nm_fx_val.append(f(x1))

        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        # uncomment this if you want function value to be within error
        # condition = abs(f(x1)) > e
        nm_error.append(x1 - prev_x0)
        # here, root value is considered for error
        condition = abs(x1 - prev_x0) > e and f(x1) != 0 and abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Initial guess
x0 = -2
# Error
e = 1e-6
# Max iterations
N = 20

# for newton raphson method
nr_epochs = []
nr_x1_val = []
nr_fx_val = []
nr_error = []

# for modified newton method
nm_epochs = []
nm_x1_val = []
nm_fx_val = []
nm_error = []

# Starting Newton Raphson Method
newtonRaphson(x0, e, N)
newtonRaphsonMultiRoot(x0, e, N)

# plt.scatter(x1_val, fx_val, s=20, marker='x')
plt.plot(nr_epochs, nr_error, label='Newton Raphson Method')
plt.plot(nm_epochs, nm_error, label='Newton Method for multiple roots')

# naming the x axis
plt.xlabel('iterations')
# naming the y axis
plt.ylabel('|xk - xk-1| (e)')
# giving a title to my graph
plt.title('Convergence plot for x0 = -2')
plt.legend()


plt.show()
