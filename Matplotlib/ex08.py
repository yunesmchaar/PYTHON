import pandas as pd
import matplotlib.pyplot as plt

# 1. Chargement du fichier CSV
df = pd.read_csv(r"C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\cours\archive (1)\athlete_events.csv")

# 2. Affichage des premières lignes
print(df.head())

# 3. Statistiques de base
print("\nStatistiques :")
print(df.describe())

# 4. Répartition hommes / femmes
sex_counts = df["Sex"].value_counts()

# 5. Diagramme circulaire
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90, colors=["skyblue", "pink"])
plt.title("Répartition des sexes des athlètes")
plt.axis("equal")
plt.show()
