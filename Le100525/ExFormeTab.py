import numpy as np

def FormeTab():
    matrice_3D=[]

    for couche in range(2):
        matrice_2D=[]
        for i in range(3):
            ligne=[]
            for j in range(4):
                nb=int(input(f"Entre votre nombre de tableau({i+1},{j+1}):"))
                ligne.append(nb)
            matrice_2D.append(ligne)
        matrice_3D.append(matrice_2D)


    print(f"Tableau de 3D utlisation de Reshape:{matrice_3D}")


FormeTab()