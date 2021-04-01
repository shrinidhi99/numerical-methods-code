import math
import matplotlib.pyplot as plt


def proterm(i, value, x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro

# Function for calculating
# divided difference table


def dividedDiffTable(x, y, n):

    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]))
    return y

# Function for applying Newton's
# divided difference formula


def applyFormula(value, x, y, n):

    sum = y[0][0]

    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i])

    return sum

# Function for displaying divided
# difference table


def printDiffTable(y, n):

    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                  end=" ")

        print("")

# Driver Code

# uncomment (return statement) function as per the question
def f(x):
    # return math.exp(-0.5 * x**2)
    return 1 / math.sqrt(1 + 25 * x ** 2)

# Pn(x) after computing for n = 5
def P_n_5(x):
    # return 0.09379 * x ** 4 - 0.4862 * x ** 2 + 0.99895
    return 0.45955 * x ** 4 - 0.88732 * x ** 2 + 0.62388

# Pn(x) after computing for n = 10
def P_n_10(x):
    # return -0.0002 * x ** 10 + 0.00254 * x ** 8 - 0.0208 * x ** 6 + 0.12499 * x ** 4 - 0.5 * x ** 2 + 1
    return -15.00417 * x ** 10 + 45.99417 * x ** 8 - 52.74827 * x ** 6 + 27.96477 * x ** 4 - 7.01038 * x ** 2 + 1

# Pn(x) after computing for n = 20
def P_n_20(x):
    # return -0.00026 * x ** 10 + 0.0026 * x ** 8 + 0.02083 * x ** 6 + 0.125 * x ** 4 - 0.5 * x ** 2 + 1
    return 1511.83622 * x ** 20 - 8392.97914 * x ** 18 + 20086.79289 * x ** 16 - 27117.16328 * x ** 14 + 22694.66896 * x ** 12 - 12197.39918 * x ** 10 + 4227.72566 * x ** 8 - 930.43382 * x ** 6 + 127.44361 * x ** 4 - 11.2958 * x ** 2 + 1

# function to compute x[i]
def x_i(i, n):
    return math.cos((i * math.pi)/n)

a = -1
b = 1
n = [5, 10, 20]

for N in n:
    # t = a

    # h = (b - a)/N

    X = []
    Y = []

    X.append(a)
    Y.append(f(a))

    # i = 0 to N (N+1 is the open interval upper bound)
    for i in range(N):
        X.append(x_i(i, N))
        Y.append(f(x_i(i, N)))
        # t += h

    print(f'For n = {N},\nx: {X}')
    print(f'For n = {N},\ny: {Y}\n\n')

    print(f'For n = {N},\nDifference Table:\n\n')
    # number of inputs given
    # n = 5
    y = [[0 for i in range(len(X))]
         for j in range(len(X))]
    x = X

    # y[][] is used for divided difference
    # table where y[][0] is used for input

    for i in range(len(Y)):
        y[i][0] = Y[i]

    # calculating divided difference table
    y = dividedDiffTable(x, y, N)

    # displaying divided difference table
    printDiffTable(y, N)

    # value to be interpolated
    value = 1

    # printing the value (Ignore this part since it is not asked in question)
    print("\nValue at", value, "is",
          round(applyFormula(value, x, y, N), 6))

# Error calculation

t = a
h = (b - a)/60

y_pred_5 = []
y_pred_10 = []
y_pred_20 = []

x_i = []
y_i = []

x_i.append(a)
y_i.append(f(a))

for i in range(60):
    x_i.append(t + h)
    y_i.append(f(t + h))
    t += h

for N in n:

    error = 0

    if N == 5:
        for i in range(len(x_i)):
            error += abs(y_i[i] - (P_n_5(x_i[i])))

            y_pred_5.append(P_n_5(x_i[i]))

        print(f'For n = {N}, error = {error}')


    elif N == 10:
        for i in range(len(x_i)):
            error += abs(y_i[i] - (P_n_10(x_i[i])))

            y_pred_10.append(P_n_10(x_i[i]))

        print(f'For n = {N}, error = {error}')

    elif N == 20:
        for i in range(len(x_i)):
            error += abs(y_i[i] - (P_n_20(x_i[i])))

            y_pred_20.append(P_n_20(x_i[i]))

        print(f'For n = {N}, error = {error}')

plt.plot(x_i, y_i, label='Y exact')
plt.plot(x_i, y_pred_5, label='Y predicted, N = 5')
plt.plot(x_i, y_pred_10, label='Y predicted, N = 10')
plt.plot(x_i, y_pred_20, label='Y predicted, N = 20')

# naming the x axis
plt.xlabel('X')
# naming the y axis
plt.ylabel('Y')
# giving a title to my graph
plt.title('Newton\'s divided difference')
plt.legend(loc='upper left')
plt.show()
