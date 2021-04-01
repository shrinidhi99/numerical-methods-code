# Name: Shrinidhi Anil Varna
# Roll no: 171CO145 
# Q no: 2

import math
from scipy.integrate import quad

# computes trapezoidal rule of given 3 points


def trapezoidal_rule(x, y):
    assert len(x) == len(y) == 2
    h = x[1] - x[0]
    return (h/2)*(y[0] + y[1])

# computes Simpson's 1/3rd rule of given 3 points


def simpson_one_third_rule(x, y):
    assert len(x) == len(y) == 3
    h = x[1] - x[0]
    return (h/3)*(y[0] + 4*y[1] + y[2])

# computes trapezoidal rule over a region extending beyond 3 points


def composite_trapezoidal_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-1):
        sum += trapezoidal_rule(x[i:i+2], y[i:i+2])
    return sum

# computes Simpson's 1/3rd rule over a region extending beyond 3 points


def composite_simpson_one_third_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-2, 2):
        sum += simpson_one_third_rule(x[i:i+3], y[i:i+3])
    return sum

# function given f(x)


def f(x):
    return (math.sin(x) / x)


N = [6, 12, 24]
X = 5

# quad function in SciPy library returns us the definite integral over a function f(x)
integral, err = quad(f, 0, 5)

quad = 1.6054 # found using MATLAB function

print(f'The integral value using Integral: {integral}')
print(f'The integral value using Quad: {quad}')


for n in N:
    x = []
    y = []
    t = 0
    x.append(0)
    y.append(1)
    for i in range(n):
        x.append(t + X/n)
        y.append(f(t + X/n))
        t += X/n

    # print(x)
    # print(y)
    T_R = composite_trapezoidal_rule(x, y)
    print(f'For n = {n}, Trapezoidal rule: {T_R}')
    print(f'Difference between Integral and Trapezoidal rule: {abs(integral - T_R)}')
    print(f'Difference between Quad and Trapezoidal rule: {abs(quad - T_R)}\n')

    S_1_3 = composite_simpson_one_third_rule(x, y)
    print(f'For n = {n}, Simpson\'s 1/3rd rule: {S_1_3}')
    print(
        f'Difference between Integral and Simpson\'s 1/3rd rule: {abs(integral - S_1_3)}')
    print(f'Difference between Quad and Simpson\'s 1/3rd rule: {abs(quad - T_R)}\n')
