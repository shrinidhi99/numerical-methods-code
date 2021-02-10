import matplotlib.pyplot as plt
import math

# Defining Function


def f(x):
    return math.cos(x) - x * math.exp(x)


def g(x):
    return -1 * (math.sin(x) + math.exp(x) + x * math.exp(x))


def falsePosition(x0, x1, e):
    step = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    prev_x2 = math.inf
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        fp_epochs.append(step)
        fp_val.append(x2)
        fp_fx_val.append(f(x2))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1

        # uncomment this if you want function value to be within error
        # condition = abs(f(x2)) > e

        # here, root value is considered for error
        # in slides, we see previous value of x2 and current value of x2

        fp_error.append(x2 - prev_x2)
        condition = abs(x2 - prev_x2) > e and f(x2) != 0
        prev_x2 = x2

    print('\nRequired root is: %0.8f' % x2)


def bisection(x0, x1, e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        b_epochs.append(step)
        b_val.append(x2)
        b_fx_val.append(f(x2))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        # uncomment this if you want function value to be within error
        # condition = abs(f(x2)) > e

        b_error.append(x1 - x0)
        # here, root value is considered for error
        condition = abs(x1 - x0) > e and f(x2) != 0

    print('\nRequired Root is : %0.8f' % x2)


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
        print('Iteration-%d, x1 = %0.8f and f(x1) = %0.6f' % (step, x1, f(x1)))
        n_epochs.append(step)
        n_val.append(x1)
        n_fx_val.append(f(x1))

        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        # uncomment this if you want function value to be within error
        # condition = abs(f(x1)) > e

        n_error.append(x1 - prev_x0)

        # here, root value is considered for error
        condition = abs(x1 - prev_x0) > e and f(x1) != 0

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


def secant(x0, x1, e, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        prev_x1 = x1
        x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        s_epochs.append(step)
        s_val.append(x2)
        s_fx_val.append(f(x2))
        s_error.append(x2 - prev_x1)

        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        # uncomment this if you want function value to be within error
        # condition = abs(f(x2)) > e

        # here, root value is considered for error
        condition = abs(x2 - prev_x1) > e and f(x2) != 0

    print('\n Required root is: %0.8f' % x2)


# Initial guess
x0 = 0
x1 = 1
# Error
e = 1e-4

N = 20

fp_epochs = []
fp_val = []
fp_fx_val = []
fp_error = []

b_epochs = []
b_val = []
b_fx_val = []
b_error = []

n_epochs = []
n_val = []
n_fx_val = []
n_error = []

s_epochs = []
s_val = []
s_fx_val = []
s_error = []


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    # false position
    falsePosition(x0, x1, e)

    # plt.scatter(fp_val, fp_fx_val, s=20, marker='x')
    plt.plot(fp_epochs, fp_error, label='False position')

    # bisection
    bisection(x0, x1, e)

    # plt.scatter(b_val, b_fx_val, s=20, marker='x')
    plt.plot(b_epochs, b_error, label='Bisection')

    # Newton Raphson Method
    newtonRaphson(x0, e, N)

    # plt.scatter(n_val, n_fx_val, s=20, marker='x')
    plt.plot(n_epochs, n_error, label='Newton Raphson')

    # Starting Secant Method
    secant(x0, x1, e, N)

    # plt.scatter(s_val, s_fx_val, s=20, marker='x')
    plt.plot(s_epochs, s_error, label='Secant')

    # print(f'epochs = {len(s_epochs)} errors = {len(s_error)}')
    # naming the x axis
    # plt.xlabel('x')
    plt.xlabel('epochs')
    # naming the y axis
    # plt.ylabel('f(x)')
    plt.ylabel('error')

    plt.legend()

    plt.show()
