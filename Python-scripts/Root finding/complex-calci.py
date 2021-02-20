import math
import cmath


def f(x):
    return x**4 - 4 * x**2 - 3 * x + 5


def muller_a(x0, x1, x2):
    a = ((x1 - x2) * (f(x0) - f(x2)) - (x0 - x2) *
         (f(x1) - f(x2))) / ((x0 - x2)*(x1 - x2)*(x0 - x1))

    print(f'a = {a}')


def muller_b(x0, x1, x2):
    b = ((x0 - x2)**2 * (f(x1) - f(x2)) - (x1 - x2)**2 *
         (f(x0) - f(x2))) / ((x0 - x2)*(x1 - x2)*(x0 - x1))

    print(f'b = {b}')


def muller_c(x2):
    c = f(x2)
    print(f'c = {c}')


muller_a(complex(-1, 0),
         complex(-1, 1),
         complex(-1, 0.9))

muller_b(complex(-1, 0),
         complex(-1, 1),
         complex(-1, 0.9))

muller_c(complex(-1, 0.9))

# x2 = -1 + 0.9j
# x3 = -1.4772872167775053 + 0.7190733089686845j
# x4 = -1.4732594924196465 + 0.8074951700914978j
