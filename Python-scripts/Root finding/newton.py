import math
import matplotlib.pyplot as plt

# Defining Function


def f(x):
    # Lecture example
    return x**3 - 1.2*x**2 - 8.19*x + 13.23   # 7*x**2 - 12*x + 1

# Defining derivative of function (f')


def g(x):
    # Lecture example
    return 3*x**2 - 2.4*x - 8.19  # 14*x - 12

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
        epochs.append(step)
        x1_val.append(x1)
        fx_val.append(f(x1))

        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        # uncomment this if you want function value to be within error
        # condition = abs(f(x1)) > e

        # here, root value is considered for error
        condition = abs(x1 - prev_x0) > e and f(x1) != 0 and abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Initial guess
x0 = 5
# Error
e = 1e-6
# Max iterations
N = 20

epochs = []
x1_val = []
fx_val = []

# Starting Newton Raphson Method
newtonRaphson(x0, e, N)

plt.scatter(x1_val, fx_val, s=20, marker='x')

# naming the x axis
plt.xlabel('x')
# naming the y axis
plt.ylabel('f(x)')
# giving a title to my graph
plt.title('Newton method x0 = 5')
plt.show()
