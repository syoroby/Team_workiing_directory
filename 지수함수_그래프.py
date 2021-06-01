##증가하는 지수함수 그래프##
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
line = plt.plot(t, t**2)
plt.setp(line, color='r', linewidth=3.0)
plt.show()
