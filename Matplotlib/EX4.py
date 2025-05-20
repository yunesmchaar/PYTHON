import matplotlib.pyplot as plt
import numpy as np

tab1=[2,4,6,2,1]
tab2=[2,4,5,2,8]

xpoint=np.array(tab1)
ypoint=np.array(tab2)
plt.plot(xpoint,ypoint)

plt.title("Plotting Without line")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.show()