import math
# <<<<<<<<<<< BASIC RULES

def I_f(x):
    return x * (math.log(x) - 1)


def trapezoidal_rule(x, y):
    assert len(x) == len(y) == 2
    h = x[1] - x[0]
    return (h/2)*(y[0] + y[1])


def simpson_one_third_rule(x, y):
    assert len(x) == len(y) == 3
    h = x[1] - x[0]
    return (h/3)*(y[0] + 4*y[1] + y[2])


def simpson_three_eighth_rule(x, y):
    assert len(x) == len(y) == 4
    h = x[1] - x[0]
    return (3*h/8)*(y[0] + 3*y[1] + 3*y[2] + y[3])


def boole_rule(x, y):
    assert len(x) == len(y) == 5
    h = x[1] - x[0]
    return (2*h/45)*(7*y[0] + 32*y[1] + 12*y[2] + 32*y[3] + 7*y[4])

# <<<<<<<<<<< COMPOSITE NEWTON COTE'S RULE

# <<<<<< Composite trapezoidal rule


def composite_trapezoidal_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-1):
        sum += trapezoidal_rule(x[i:i+2], y[i:i+2])
    return sum

def f(x):
    return (math.sin(x) / x)

N = [6, 12, 24]
X = 5

for n in N:
    x = []
    y = []
    t = 0
    x.append(0)
    y.append(1)
    for i in range(n):
        x.append(t + X/n)
        y.append(f(t + X/n))

    print(x)
    print(y)
    
# x = [7.47, 7.48, 7.49, 7.50, 7.51, 7.52]
# y = [1.93, 1.95, 1.98, 2.01, 2.03, 2.06]

T_R = composite_trapezoidal_rule(x, y)
print(f'Trapezoidal rule: {T_R}')

# <<<<<< Composite Simpson's one-third rule


def composite_simpson_one_third_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-2, 2):
        sum += simpson_one_third_rule(x[i:i+3], y[i:i+3])
    return sum


x = [4, 4.2, 4.4, 4.6, 4.8, 5, 5.2]

y = []

for i in x:
    y.append(math.log(i))


# x = [7.47, 7.48, 7.49, 7.50, 7.51, 7.52]
# y = [1.93, 1.95, 1.98, 2.01, 2.03, 2.06]
# x = [0, 0.25, 0.5, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00]
# y = [0.5, 0.4923, 0.4706, 0.4384, 0.4, 0.3596, 0.32, 0.2832, 0.25]

S_1_3 = composite_simpson_one_third_rule(x, y)
print(f'Simpson\'s 1/3rd rule: {S_1_3}')

# <<<<<< Composite Simpson's three-eighth rule


def composite_simpson_three_eighth_rule(x, y):
    assert len(x) == len(y)
    sum = 0
    for i in range(0, len(x)-3, 3):
        sum += simpson_three_eighth_rule(x[i:i+4], y[i:i+4])
    return sum


x = [4, 4.2, 4.4, 4.6, 4.8, 5, 5.2]

y = []

for i in x:
    y.append(math.log(i))

S_3_8 = composite_simpson_three_eighth_rule(x, y)
print(f'Simpson\'s 3/8th rule: {S_3_8}')

# <<<<<< Composite Boole's rule


# def composite_boole_rule(x, y):
#     assert len(x) == len(y)
#     sum = 0
#     for i in range(0, len(x)-4, 4):
#         sum += simpson_three_eighth_rule(x[i:i+5], y[i:i+5])
#     return sum


# Exact value of the integral f(exact)
f_exact = I_f(5.2) - I_f(4)
print(f'Exact value of the interval: {f_exact}')

print(f'Absolute error: Trapezoidal rule: {abs(f_exact - T_R)}')
print(f'Absolute error: Simpson\'s 1/3rd rule: {abs(f_exact - S_1_3)}')
print(f'Absolute error: Simpson\'s 3/8th rule: {abs(f_exact - S_3_8)}')
