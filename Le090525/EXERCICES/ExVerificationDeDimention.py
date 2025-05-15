from array import array

import numpy as np
lignes=int(input(f"Entrez votre ligne:"))
colonnes=int(input(f"Entrez votre colonne:"))
matrice=[]
def VerificationDeDimension():

  for i in range(lignes):
      ligne = []
      for j in range(colonnes):
          nb=int(input(f"Entrez votre valeur ({i+1},{j+1}):"))
          ligne.append(nb)
      matrice.append(ligne)
  array=np.array(matrice)
  print(f"le tableau original:{array}")
  print(f"le tableau apre convertion est:{np.shape(array)}")
  if array.ndim==1:
      print("le tableau a de un dimention.")
  elif array.ndim==2:
      print(f"le tableau a de deux dimention.")
  else:
      print(f"le tableau n'est pas de deux dimention ou un seulle dimention.")





