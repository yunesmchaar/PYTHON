import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
# Taille de la figure
plt.figure(figsize=(12, 8))
Mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"]
Eau = [30, 28, 35, 40, 38, 36]

plt.subplot(2,2,1)
plt.plot(Mois,Eau)
plt.title("Courbe sur un meme graphique")
plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.grid(True)
plt.tight_layout()


Filieres = ["Informatique", "Maths", "Physique", "Biologie"]
NbDetudiants = [120, 90, 100, 80]

plt.subplot(2,2,2)
plt.bar(Filieres,NbDetudiants)
plt.title("Diagramme en barres")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.grid(True)
plt.tight_layout()

Ages = [22, 25, 30, 35, 40, 22, 27, 29, 30, 31, 35, 38, 40, 45, 50, 22]
plt.subplot(2,2,3)
plt.hist(Ages,width=0.2,color='r')
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.grid(True)
plt.tight_layout()

Categories = ["Loyer", "Nourriture", "Transport", "Loisirs", "Autres"]
Depenses = [500, 200, 100, 150, 50]

plt.subplot(2,2,4)
plt.pie(Depenses,labels=Categories)
plt.title("Diagramme circulaire")
plt.grid(True)
plt.tight_layout()

plt.show()


