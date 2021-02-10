import math
import matplotlib.pyplot as plt

# Defining Function


def f(x):
    # Lecture example
    # initial x0=1, x1=2
    return x**3 - 10*x**2 + 5  # x**4 - 11*x + 8

# Implementing False Position Method (Regula-Falsi)


def falsePosition(x0, x1, e):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    prev_x2 = math.inf
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        epochs.append(step)
        x2_val.append(x2)
        fx_val.append(f(x2))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1

        # uncomment this if you want function value to be within error
        # condition = abs(f(x2)) > e

        # here, root value is considered for error
        # in slides, we see previous value of x2 and current value of x2
        condition = abs(x2 - prev_x2) > e and f(x2) != 0
        prev_x2 = x2

    print('\nRequired root is: %0.8f' % x2)


# Initial guess
x0 = 0.2
x1 = 1.2
# Error
e = 1e-5

epochs = []
x2_val = []
fx_val = []

# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0, x1, e)

    plt.scatter(x2_val, fx_val, s=20, marker='x')

    # naming the x axis
    plt.xlabel('x')
    # naming the y axis
    plt.ylabel('f(x)')
    # giving a title to my graph
    plt.title('Regula-Falsi (False-position)')
    plt.show()
