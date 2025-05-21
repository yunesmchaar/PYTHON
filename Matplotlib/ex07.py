import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
Depenses = [500, 200, 100, 150, 50]
Categories = ["Loyer", "Nourriture", "Transport", "Loisirs", "Autres"]


plt.pie(Depenses,labels=Categories,startangle=90)
plt.title("Diagramme circulaire")
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()