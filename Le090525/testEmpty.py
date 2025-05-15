import numpy as np

def testE():
    print(f"***********le constructeur empty()********************")
    print(f"le constructeur empty() sert a creer un tableau vide, sans initialiser ses valeurs")
    print(f"Df:np.empty(shape,dtype=float")
    print(f"shape:les dimensions du tableau ex:(2,3) pour 2 lignes et 3 colonns")
    print(f"dtype:le type des donnees (float,int,etc).")
    print(f"Exemple pratique:")
    print(f"{np.empty((4,6),dtype=int)}")