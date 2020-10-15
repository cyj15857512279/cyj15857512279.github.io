  
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-35.0, 35.0, 0.01)
y = np.exp(-0.01*x)*np.cos(x)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(x, y)
plt.show()
