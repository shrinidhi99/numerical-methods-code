import matplotlib.pyplot as plt
import math
import matplotlib
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

courses = ['i,a,5', 'i,a,10', 'i,a,20',
           'ii,a,5', 'ii,a,10', 'ii,a,20',
           'i,b,5', 'i,b,10', 'i,b,20',
           'ii,b,5', 'ii,b,10', 'ii,b,20']

values = [23.98150771838166, 23.99816321916445, 45.00729358076398,
          4.35324560637725, 7.688862598505375, 57.14138022621446,
          23.999473065813763, 23.996268326969588, 24.396316336365906,
          4.760413211060489, 1.3923792218984004, 0.14266857551238635]

plt.bar(courses, values, width=0.2)

plt.xlabel("[Function, Subquestion, n]")
plt.ylabel("Error")
# plt.title(" various pre-trained models")
plt.xticks(rotation=75)

plt.show()
