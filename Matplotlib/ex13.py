import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

produits = ['Produit A', 'Produit B', 'Produit C', 'Produit D']
ventes = [350, 200, 150, 100]

plt.figure(figsize=(10,5))
plt.pie(ventes,labels=produits,autopct='%1.1f%%')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.axis('equal')
plt.show()