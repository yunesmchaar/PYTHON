import matplotlib.pyplot as plt

import numpy as np

from PYTHON.Matplotlib.EX4 import ypoint

xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.title("MUltiple Points")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.show()