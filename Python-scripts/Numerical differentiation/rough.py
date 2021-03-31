import math
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x)


h = [0.1, 0.05, 0.01, 0.001]

for x in h:
    print(round(math.cos(0.9) - (f(0.9 + x) - f(0.9 - x))/(2 * x), 6))

x = []
y = []

for i in range(10):
    x.append(i)
    y.append((1 - 2 ** i)/(1 - 2))

plt.scatter(x, y)
plt.show()