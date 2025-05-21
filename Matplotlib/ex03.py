
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

jours=["lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
Temperatures=[15,17,14,20,22,19,18]

plt.plot(jours,Temperatures,'o-k',mec='r',mfc='k')
plt.title("Courbe simple")
plt.xlabel("Axe X")
plt.ylabel("Axe y")

plt.grid(True)
plt.tight_layout()
plt.show()