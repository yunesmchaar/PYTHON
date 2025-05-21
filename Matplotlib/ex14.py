import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

plt.figure(figsize=(10,10))
jours = list(range(1, 11))
athlete1 = [10, 9.8, 9.7, 9.5, 9.4, 9.3, 9.5, 9.6, 9.4, 9.2]
athlete2 = [11, 10.5, 10.3, 10.2, 10.1, 9.9, 9.8, 9.7, 9.6, 9.5]
liste=[]
for i in range(len(athlete1)):
    result=athlete2[i]-athlete1[i]
    liste.append(result)
plt.plot(jours,athlete1,'o-r',mec='k',mfc='g',label='athlete1')
plt.plot(jours,athlete2,'o-g',mec='r',mfc='k',label='athlete2')
plt.plot(jours,liste,'o-b',mec='g',mfc='k',label='athlete2-athlete1')
plt.title("Comparaison de deux series")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()