import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

xliste=[]
yliste=['Rabat','Sale','khemisat','Kenitra','CASA','Khemissat','Tange','Hossima','Warzazat','Dakhla']
zliste=[]

for i in range(10):
    NbEtudiant=random.randint(0,10)
    xliste.append(NbEtudiant)
print(f"{xliste}")

for j in range(len(yliste)):
    Ville=random.choice(yliste)
    zliste.append(Ville)
print(f"{zliste}")
plt.plot(xliste,zliste)
plt.title("le Diagramme de histogramme")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
#plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

