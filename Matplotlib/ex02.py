import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xliste=list(range(11))

y1=[i**2 for i in xliste]
y2=[i**3 for i in xliste]

plt.subplot(1,2,1)
plt.plot(xliste,y1,'b-')
plt.title("Carre de Nombres")

plt.xlabel("Valeur de x")
plt.ylabel("Carre de x")
plt.subplot(1,2,2)
plt.plot(xliste,y2,'r:')
plt.show()