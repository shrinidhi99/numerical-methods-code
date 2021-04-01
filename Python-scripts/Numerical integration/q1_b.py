import math


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
    return math.exp(-0.5 * x**2)
    # return 1 / math.sqrt(1 + 25 * x ** 2)

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
