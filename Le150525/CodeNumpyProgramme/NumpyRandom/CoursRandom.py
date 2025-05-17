from dataclasses import replace

from numpy import random
#randint
print(f"la forme general de randint est numpy.random.randint(low,high=none,size=none)")
#generer un nombre aleatoire entre 0 et 79
x=random.randint(80,None,None)
print(f"Nombre aleatoire :{x}")

#generer un  nombre aleatoire  entre 1 et 99
x=random.randint(1,99,size=None)
print(f"le nombre aleatoire entre 1 et 99 :{x}")

#generer un nombre aleatoire de tableau de 1 dimension le nombre entre 1 et 99
x=random.randint(1,99,size=8)
print(f"la tableaux de size 8 element :{x}")
print(f"nombre de dimension:{x.ndim}")

#generer un tableau de 2 dimension des nombres entre 1 et 99 et de size = 8
x=random.randint(1,99,size=(1,8))
print(f"Tableau de 2 Dimension :{x}")
print(f"nombre de dimension:{x.ndim}")

#rand()

#generer un element aleatoire entre 0 et 1 de type float
x=random.rand()
print(f"le nombre aleatoire de type float :{x}")

#generer un nombre aleatoire entre 0 et 1 de type float mais de tableau de 1 dimension
x=random.rand(5)
print(f"Tableau de 5 elements:{x}")

#generer les elements de tableau aleatoire de size entre 2 ligne 3 colonne
x=random.rand(1,2)
print(f"les elements de tableau de 2 ligne et 3 colonne est {x}")

#Choice()

#tires un element au hasard depuis une liste
liste=["A","B","C"]
x=random.choice(liste)
print(f"tires un element au hasard dans c'est liste:{x}")

#tirer 5  entiers entre 0 et 9 (avec remise)
x=random.choice(9,size=3)
print(f"tirer le 5 entiers entre 0 et 9 avec remise :{x}")

#tirer 5 elements sans repetition
x=random.choice(9,size=4,replace=False)
print(f"tirer 5 elements sans repetition :{x}")


#tirer 5 elements avec probabilite
x=random.choice(liste,len(liste),p=[0.1,0.1,0.8],replace=False)
print(f"Tirer 5 elements avec probabilite :{x}")

#



