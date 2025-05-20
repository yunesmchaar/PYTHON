import matplotlib.pyplot as plt

# Données simples
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

# Tracer la courbe
plt.plot(x, y, label="Courbe simple", color='blue', marker='o')

# Ajouter un titre et des labels
plt.title("Exemple de graphique avec Matplotlib")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")

# Afficher la légende
plt.legend()

# Afficher le graphique
plt.show()
