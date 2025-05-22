import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

jeurs=[]
mois=['A','B','C','D','E','F','G','H','I','J']
newmois=[]
for i in range(10):
    nb=random.randint(0,100)
    jeurs.append(nb)
for i in range(10):
    nbr=random.choice(mois)
    newmois.append(nbr)

plt.hist(mois,jeurs)
plt.title("TEST DE REQUEPERATION")
plt.xlabel("AXE Jeurs")
plt.ylabel("AXE Mois")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
