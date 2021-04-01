import matplotlib.pyplot as plt
import math
import matplotlib
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# courses = ['i,a,5', 'i,a,10', 'i,a,20',
#            'ii,a,5', 'ii,a,10', 'ii,a,20',
#            'i,b,5', 'i,b,10', 'i,b,20',
#            'ii,b,5', 'ii,b,10', 'ii,b,20']

# values = [23.98150771838166, 23.99816321916445, 45.00729358076398,
#           4.35324560637725, 7.688862598505375, 57.14138022621446,
#           23.999473065813763, 23.996268326969588, 24.396316336365906,
#           4.760413211060489, 1.3923792218984004, 0.14266857551238635]

quad_tr = [0.049864654948662546, 0.054086781061416955, 0.055124436206535]
integral_tr = [0.005604100106663, 0.001381973993908, 0.000344318848789]

quad_s_1_3 = [0.049864654948662, 0.049864654948662, 0.055124436206535]
integral_s_1_3 = [0.000429650610723, 2.5401377009348636e-05, 1.5661995831361963e-06]

n = [6, 12, 24]

# plt.bar(courses, values, width=0.2)
plt.plot(n, quad_tr, label='Quad error TR')
plt.plot(n, integral_tr, label='Integral error TR')

plt.plot(n, quad_s_1_3, label='Quad error S 1/3rd')
plt.plot(n, integral_s_1_3, label='Integral error S 1/3rd')

plt.xlabel("[Function, Subquestion, n]")
plt.ylabel("Comparison")
# plt.title(" various pre-trained models")
# plt.xticks(rotation=75)
plt.legend()
plt.show()
