import matplotlib.pyplot as plt

# Données
ages = [22, 25, 28, 30, 25, 26, 32, 34, 40, 41, 39, 45, 50, 29, 33, 30, 31, 35]
# Création de l'histogramme
plt.figure(figsize=(8, 5))
plt.hist(ages, bins=6, color='skyblue', edgecolor='black')
# Mise en forme
plt.title("Distribution des âges des employés")
plt.xlabel("Tranche d'âge")
plt.ylabel("Nombre d'employés")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Affichage
plt.show()
