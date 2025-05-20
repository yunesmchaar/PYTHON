import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([1,3,4,7,8])
plt.plot(ypoints,'o-k',ms=8,mec='r')
plt.title("Markers")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.show()