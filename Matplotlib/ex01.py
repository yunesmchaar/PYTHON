import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd
xliste=[random.randint(0,10) for _ in range(10)]
yliste=[]
nb = len(xliste)
for i in range(nb):
    yliste.append(xliste[i]*xliste[i])
print(yliste)

plt.plot(xliste,yliste)
plt.title("Carre de Nombres")
plt.xlabel("Valeur de X")
plt.ylabel("Carre de X")
plt.show()