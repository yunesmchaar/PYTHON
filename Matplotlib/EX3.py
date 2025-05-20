import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints= np.array([0,250])

plt.title("My first matplotlib")
plt.xlabel("Axe X")
plt.ylabel(" Axe Y")
plt.plot(xpoints,ypoints)
plt.show()