import matplotlib.pyplot as plt

# Années de 2010 à 2020 (11 ans)
annees = list(range(2010, 2021))

# Données des magasins (11 valeurs chacune)
magasin1 = [70719, 43747, 56860, 66905, 50591, 67210, 47882, 76576, 56627, 79337, 81200]
magasin2 = [73589, 72720, 90760, 89543, 89477, 92325, 80173, 75448, 69521, 86187, 87500]

# Création du graphique
plt.figure(figsize=(10, 6))
plt.plot(annees, magasin1, label="Magasin 1", marker='o', color='b')
plt.plot(annees, magasin2, label="Magasin 2", marker='s', color='g')

plt.title("Tracer les gains de deux magasins sur 11 ans")
plt.xlabel("Années")
plt.ylabel("Gains ($)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
