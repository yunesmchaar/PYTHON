import random
import numpy as np
import matplotlib.pyplot as plt

print("HELLO, I am Python")

noms = ['A', 'B', 'C', 'D', 'E', 'F']
notes = [10, 18, 13, 16, 11, 18]

fig, ax = plt.subplots()  # Crée une figure et un axe
fig.patch.set_facecolor('lightgreen')  # Arrière-plan de la figure
ax.set_facecolor('green')              # Arrière-plan du graphe (zone des données)

ax.plot(noms, notes, color='white')    # Courbe en blanc pour bien contraster
ax.set_xlabel('Axe x')
ax.set_ylabel('Axe y')
ax.set_title('Notes des élèves')
plt.show()

