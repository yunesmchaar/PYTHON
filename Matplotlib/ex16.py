import matplotlib.pyplot as plt

# Données
annees = list(range(2010, 2021))
pib = [2.5, 2.6, 2.8, 3.0, 3.2, 3.4, 3.5, 3.6, 3.7, 3.3, 2.1]

# Création du graphique
plt.figure(figsize=(10, 5))
plt.plot(annees, pib, marker='o', linestyle='-', color='blue', label="PIB (en milliers de milliards $)")

# Annotation du point de crise en 2020
plt.annotate("Crise COVID",
             xy=(2020, 2.1),
             xytext=(2017, 2.5),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10, color='red')

# Mise en forme
plt.title("Évolution du PIB de 2010 à 2020")
plt.xlabel("Années")
plt.ylabel("PIB (en milliers de milliards $)")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Affichage
plt.show()
