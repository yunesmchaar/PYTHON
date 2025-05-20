
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Chargement du dataset iris (fourni par seaborn)
iris = sns.load_dataset("iris")

# Affichage de la heatmap des corrélations
sns.heatmap(iris.corr(), annot=True, cmap="coolwarm")
plt.title("Corrélation entre les variables (Iris)")
plt.show()
