import numpy as np
import matplotlib.pyplot as plt
import math

x0 = 3.9
r = 0.2022
t = np.arange(1790, 2000, 10)

y = [3.9, 5.3, 7.3, 9.6, 12.9, 17.1, 23.2, 31.4, 38.6, 50.2, 62.9, 76.0, 92.0, 106.5, 123.2, 131.7, 150.7, 179.3, 204.0, 226.5, 251.4, 281.4]
f = x0*pow(math.e, r*((t-1790)/10))
plt.plot(t, y[1:22], 'ro')
plt.plot(t, f)
plt.show()