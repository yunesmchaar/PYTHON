import numpy as np

lignes = int(input("Entrez le ligne de votre tableau:"))
colonnes = int(input("Entrez votre colonnes de votre tableau:"))
matrices=[]
def VerificationDim():
    for i in range(lignes):
        ligne=[]
        for j in range(colonnes):
            nb=int(input("Donner les element de votre tableau:"))
            ligne.append(nb)
        matrices.append(ligne)
    Tab=np.array(matrices)
    print(f"Tableau Original:{Tab}")

    print(f"le Tableau calculer :{np.shape(Tab)}")
    if np.ndim(Tab)==1:
         print(f"votre tableau a de un dimention")
    elif np.ndim(Tab)==2:
        print(f"votre tableau a de deux dimention")
    else:
        print(f"votre tableaux de plus de dimention")
