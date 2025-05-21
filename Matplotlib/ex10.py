import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

liste=[]
for i in range(10):
    nbVisiteurs=random.randint(0,10)
    liste.append(nbVisiteurs)

print(f"votre elements de tableau {liste}")

plt.plot(liste,'o-r',mec='k',mfc='r',label='NbVisiteurs')
plt.title("Courbe avec personnalisation")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()