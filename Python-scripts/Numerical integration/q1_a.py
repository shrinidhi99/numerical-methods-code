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

# uncomment function as per the question


def f(x):
    # return math.exp(-0.5 * x**2)
    return 1 / math.sqrt(1 + 25 * x ** 2)

# In P_n(x) functions, the first return statement refers to first subquestion and the second one refers to second subquestion.
# Uncomment as per requirements

# Pn(x) after computing for n = 5


def P_n_5(x):
    # return 0.0995 * x ** 4 - 0.4927 * x ** 2 + 0.9997
    return 1.0769 * x ** 4 - 1.65226 * x ** 2 + 0.77147

# Pn(x) after computing for n = 10


def P_n_10(x):
    # return 0.0026 * x ** 8 - 0.0208 * x ** 6 + 0.125 * x ** 4 - 0.5 * x ** 2 + 1
    return -103.19031 * x ** 10 + 233.0467 * x ** 8 - 182.6443 * x ** 6 + 61.48831 * x ** 4 - 9.50428 * x ** 2 + 1

# Pn(x) after computing for n = 20


def P_n_20(x):
    # return -0.00026 * x ** 10 + 0.0026 * x ** 8 - 0.02083 * x ** 6 + 0.125 * x ** 4 + 0.5 * x ** 2 + 1
    return 87198.71515 * x ** 20 - 339918.55971 * x ** 18 + 552203.28856 * x ** 16 - 488310.7409 * x ** 14 + 258107.5959 * x ** 12 - 84586.42876 * x ** 10 + 17377.06324 * x ** 8 - 2249.68398 * x ** 6 + 190.19746 * x ** 4 - 12.25084 * x ** 2 + 1


a = -1
b = 1
n = [5, 10, 20]

for N in n:
    t = a

    h = (b - a)/N

    X = []
    Y = []

    X.append(a)
    Y.append(f(a))

    for i in range(N):
        X.append(t + h)
        Y.append(f(t + h))
        t += h

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
