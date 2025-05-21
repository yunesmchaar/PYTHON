import matplotlib.pyplot as plt
import numpy as np
import pandas as pb

xpoint=np.array([1,2,5,7,9])
ypoint=np.array([2,3,5,7,3])

plt.subplot(1,2,1)
plt.plot(xpoint,ypoint)

xpoint=np.array([1,2,4,5,7])
ypoint=np.array([2,1,4,2,5])

plt.subplot(1,2,2)
plt.plot(xpoint,ypoint)
plt.show()
