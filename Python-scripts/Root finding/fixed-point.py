# Fixed Point Iteration Method
import math
import matplotlib.pyplot as plt


def f(x):
    # Lecture example
    return x**3 + x**2 - 1

# Re-writing f(x)=0 to x = g(x)


def g(x):
    # Lecture example
    return 1 / math.sqrt(1 + x)

# Implementing Fixed Point Iteration Method


def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        prev_x0 = x0

        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))

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
        condition = abs(x1 - prev_x0) > e and f(x1) != 0

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Initial guess
x0 = 0.5
# Error
e = 1e-4
# Max iterations
N = 10

epochs = []
x1_val = []
fx_val = []

# Starting Fixed point Method
fixedPointIteration(x0, e, N)

plt.scatter(x1_val, fx_val, s=20, marker='x')
# naming the x axis
plt.xlabel('x')
# naming the y axis
plt.ylabel('f(x)')
# giving a title to my graph
plt.title('Fixed point iteration')
plt.show()