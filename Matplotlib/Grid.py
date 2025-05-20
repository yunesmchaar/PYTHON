import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,3,6,7,8,9])

plt.plot(xpoints,'o-r',ms='12',mec='r',mfc='k')
plt.title("Tableau Grid")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.grid(color='green',linestyle='-',linewidth=0.5)
plt.show()