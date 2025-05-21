import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random



filieres = ["Informatique","Maths","Physique","Biologie"]
NombreDetudiants=[120,90,100,80]

plt.bar(filieres,NombreDetudiants,width=0.1,color='b',label='Nombre')
plt.plot(filieres,NombreDetudiants,'o-',mec='k',mfc='r')
plt.title("Diagramma en barres")
plt.xlabel("Axe x")
plt.ylabel("Axe y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
