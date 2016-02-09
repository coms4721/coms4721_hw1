import pyplot

import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

a = [1,3,5,7]
b = [11,-2,4,19]
plt.pyplot.scatter(a,b)
plt.scatter(a,b)

plt.show()
c = [1,3,2,1]
plt.errorbar(a,b,yerr=c, linestyle="None")

plt.show()