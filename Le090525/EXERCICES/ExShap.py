import numpy as np

from Le090525.EXERCICES.ExVerificationDeDimention import matrice

def affichageForme():
    nb=int(input("Entrez un nombre:"))
    liste=[]
    for i in range(nb):
        nbr=int(input(f"Entrez le nombre {i+1}:"))
        liste.append(nbr)
        #utilisation array pour convertire la liste d'un forme d'un tableau de numpy
        array=np.array(liste)
    print(f"Tableau Original:{array}")
    print(f"{np.shape(array)}")



