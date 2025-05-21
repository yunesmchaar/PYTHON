from cProfile import label

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

mois=["Jan","Fev","Mar","Avr","Mai","Juin"]
eau=[30,28,35,40,38,36]
electricite=[300,280,310,330,320,310]
plt.plot(mois,eau,'o-g',mec='k',label='Eau (m3)')
plt.plot(mois,electricite,'o-b',mec='r',label="Electricite (kwh)")
plt.title("Deux courbes sur un meme graphique")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.legend()
plt.grid(True)
#plt.tight_layout()
plt.show()