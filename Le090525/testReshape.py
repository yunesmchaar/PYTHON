
"""
import numpy as np

choix = input("Votre choix (Df ou Exemple) : ")

def testReshape(choix):
    match choix:
        case "Df":
            return "Reshape signifie changer la forme (les dimensions) d'un tableau ou d'une matrice sans modifier son contenu."
        case "Exemple":
            a = np.array([10, 16, 14, 12, 13, 15])
            b = a.reshape((1, 6))  # 2 lignes, 3 colonnes = 6 éléments
            return f"Tableau original : {a}\nTableau après reshape :\n{b}"
        case _:
            return "Choix invalide."

# Exécution
print(testReshape(choix))

"""

