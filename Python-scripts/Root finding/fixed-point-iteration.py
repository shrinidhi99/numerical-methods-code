import math
import matplotlib.pyplot as plt

x = 0.5

x_l = []
y_l = []

for i in range(50):
    if i == 0:
        g_x = 1 / math.sqrt(1 + x)  # math.exp(-1*x) #* math.cos(x)
    else:
        g_x = 1 / math.sqrt(1 + g_x)  # math.exp(-1*g_x) #* math.cos(g_x)
    # print(g_x)
    x_l.append(i)
    y_l.append(g_x)

print(g_x)
plt.plot(x_l, y_l)

# naming the x axis
plt.xlabel('iterations')
# naming the y axis
plt.ylabel('g(x)')
# giving a title to my graph
plt.title('Fixed point iteration')
plt.show()
